"""
Module with a single class 'ConstraintGrammar'.  
The class represents a constraint-based encoding of a context-free grammar given in 
SyGuS problems: https://sygus.org/  

General concept:  
The main components are:  
(i) A set of variables (boolean here) that correspond to various decisions on rule expansions in the grammar.  
(ii) An 'evaluation' function that corresponds valuations over variables in (i) to the yield of the grammar that 
results from following the corresponding rule expansions.  
Refer to the package description for the roles and usage of these components.  

Detailed description of implementation:  
The class in this module implements (i) by representing the grammar as a tree-like structure rooted at 
the start symbol. Each nonterminal node has a child corresponding to each of its production rules. A boolean 
variable represents the choice of picking a given rule for expansion. These production rules can themselves 
have other nonterminals occurring in them that need to be expanded, and these will have 'subtrees' of their own. 
The boolean variables are unique to each rule in any subtree, even if the roots of two subtrees have 
the same nonterminal (and therefore have the same rules). This structure is finite if the grammar is finite, and 
as such objects of this implementation of the ConstraintGrammar class can only be those corresponding to 
finite grammars. Lastly, each occurrence of a nonterminal anywhere in this structure is renamed to a 
unique symbol. Note that the construction is completely agnostic to the types of the nonterminals.  

The tree-like structure then represents the total relationship between nonterminals and expansions for any possible 
yield of the grammar, where a particular yield corresponds to the values of all the aforementioned boolean variables. 
This relationship can be presented in the form of a constraint to an SMT solver, which achieves component (ii) 
above.  
"""

from src.SyGuSGrammar import track_nonterminals_one_step, SyGuSGrammar
import src.lisplike as lisplike


class NonsenseValuationException(Exception):
    """
    This exception is raised when valuations on the constraint-based representation does not have a valuation 
    that is meaningful as a yield of the grammar.  
    """
    pass


class ConstraintGrammar:
    """
    Basic class that generates a constraint-based representation of a SyGuS grammar. 
    """

    def __init__(self, sygus_grammar):
        if not isinstance(sygus_grammar, SyGuSGrammar):
            raise TypeError('SyGuSGrammar expected.')
        elif not sygus_grammar.is_finite():
            raise ValueError('Grammar is not finite. Unsupported.')
        # Preprocessing
        nonterminals = sygus_grammar.get_nonterminal_set()

        # Essential attributes
        self.sygus_grammar = sygus_grammar
        # Dictionary of boolean variables representing choices of rules for various copies of nonterminals.
        # Each boolean variable points to a unique expansion rule for some nonterminal in the grammar.
        # Keys are the names of the boolean variables as strings. Values are a list of strings.
        # The list is of names of nonterminal copies corresponding to the actual nonterminals in the production rule 
        # pointed to by the boolean variable. The order of the copies is the order in which the nonterminals appear 
        # in the SyGuSGrammar.post dictionary.
        self.boolvars = None
        # Dictionary simlar to self.boolvars representing the catch case of the final replacement rule choice.
        # Keys are the names of nonterminal copies whose catch case is contained in the value.
        # Values are the names of nonterminal copies corresponding to the actual nonterminals in the (final)
        # production rule for the nonterminal copy key.
        self.boolcatch = None
        # Dictionary of copies of nonterminals.
        # The keys are the names of the copies as strings. Values are a tuple (parent, list of boolvars)
        # Parent is the original nonterminal for which the key is a copy, and the list is of boolean variables 
        # corresponding to the choice of each production rule.The order of boolvars is the order in which 
        # the rules appear in the result of SyGuSGrammar.get_ordered_rule_dict.
        self.symbols = None
        # Starting symbol to traverse the constraint-based representation
        self.starting_symbol = None

        # Internal attributes (should not exposed by any methods)
        self._post = track_nonterminals_one_step(sygus_grammar)
        self._rule_dict = sygus_grammar.get_ordered_rule_list()

        # Attributes for caching useful values
        # self.post = track_nonterminals_one_step(sygus_grammar)

    def compute_constraint_encoding(self):
        """
        Compute the constraint-based representation of the grammar given by the encapsulated SyGuSGrammar object.  
        The computation is entirely internal to the class and the results can only be accessed by getter/printer 
        methods.  
        :return: None  
        """
        # Method is decoupled from initialisation because there may be functions in future versions that make
        # changes to the object fields before needing to compute the constraint-based representation.
        self.boolvars = dict()
        self.boolcatch = dict()
        # Counter for creating fresh boolean variable names
        boolcounter = 0
        self.symbols = dict()
        start_symbol = self.sygus_grammar.get_start_symbol()
        # Counters for creating fresh nonterminal copy names
        nonterminal_copy_counter = {nonterminal: 0 for nonterminal in self.sygus_grammar.get_nonterminal_set()}
        synthfun_name = self.sygus_grammar.get_name()

        # Worklist algorithm to compute self.boolvars and self.symbols such that they are populated with the 
        # intended meaning. Refer to the extensive comments in the __init__ function for what these variables 
        # should contain.
        # Worklist will contain pairs (nonterminal, nonterminal_copy). Initial pair is the start symbol and its copy.
        start_symbol_initial_copy = _nonterminal_copy_name(start_symbol,
                                                           nonterminal_copy_counter[start_symbol],
                                                           synthfun_name)
        self.starting_symbol = start_symbol_initial_copy
        nonterminal_copy_counter[start_symbol] = nonterminal_copy_counter[start_symbol] + 1
        worklist = {(start_symbol, start_symbol_initial_copy)}
        while worklist:
            nonterminal, nonterminal_copy = worklist.pop()
            # Invent as many new boolean variables as rules (minus one), and add the entry to symbols
            rule_list = self._rule_dict[nonterminal]
            num_rules = len(rule_list)
            new_boolvars = []
            # If there is just one rule, no need for boolean variables
            for _ in range(num_rules-1):
                fresh_boolvar_number = boolcounter
                fresh_boolvar_name = _boolvar_name(fresh_boolvar_number, synthfun_name)
                boolcounter = boolcounter + 1
                new_boolvars = new_boolvars + [fresh_boolvar_name]
            self.symbols[nonterminal_copy] = (nonterminal, new_boolvars)

            # For each rule create new nonterminal copies and add the entry to boolvars.
            for i in range(num_rules):
                post_symbols = self._post[nonterminal][i]
                post_symbol_copies = []
                for symbol in post_symbols:
                    fresh_nonterminal_number = nonterminal_copy_counter[symbol]
                    fresh_nonterminal_name = _nonterminal_copy_name(symbol, fresh_nonterminal_number, synthfun_name)
                    nonterminal_copy_counter[symbol] = nonterminal_copy_counter[symbol] + 1
                    post_symbol_copies = post_symbol_copies + [fresh_nonterminal_name]
                    # Add the copies with the original symbols to the worklist.
                    worklist.add((symbol, fresh_nonterminal_name))
                if i != num_rules - 1:
                    boolvar_name = new_boolvars[i]
                    self.boolvars[boolvar_name] = post_symbol_copies
                else:
                    # Catchall case for symbol copies of last production rule
                    # Same as the entry in the if branch but made in self.boolcatch
                    self.boolcatch[nonterminal_copy] = post_symbol_copies

    def evaluate(self, valuation):
        """
        Apply the given valuation on boolean variables to the representation. The result is an expression from 
        the grammar.  
        :param valuation: dict {string: bool}  
        :return: lisplike.is_lisplike  
        """
        ordered_rule_dict = self._rule_dict
        starting_symbol = self.starting_symbol
        # Construct pairs containing each symbol and the expression it expands to based on the valuation
        substitution_pairs = []
        for symbol in self.symbols:
            original_symbol, rule_choice_boolvars = self.symbols[symbol]
            try:
                chosen_rule_index = next(i for i in range(len(rule_choice_boolvars))
                                         if valuation[rule_choice_boolvars[i]])
                chosen_rule = ordered_rule_dict[original_symbol][chosen_rule_index]
                # Substitute the occurrences of nonterminals in the rule with their copies for further evaluation
                # Order of boolvars and _post have been coordinated with the order of the rules. Refer __init__.
                nonterminals_in_rule = self._post[original_symbol][chosen_rule_index]
                nonterminal_copies = self.boolvars[rule_choice_boolvars[chosen_rule_index]]
            except StopIteration:
                # All boolvars are False; catchall case
                # Choose the last expansion rule in the ordered list of rules
                chosen_rule = ordered_rule_dict[original_symbol][-1]
                nonterminals_in_rule = self._post[original_symbol][-1]
                nonterminal_copies = self.boolcatch[symbol]
            substitution = lisplike.substitute(chosen_rule, list(zip(nonterminals_in_rule, nonterminal_copies)))
            substitution_pairs = substitution_pairs + [(symbol, substitution)]

        # Auxiliary function to apply valuations and build the result recursively
        def evaluate_aux(expr=None):
            if expr is None:
                expr = starting_symbol
            # If there are any nonterminals in the expression substitute them with the expansion rules recursively
            expanded_expr = lisplike.substitute(expr, substitution_pairs)
            # There are only three choices: 
            # (i) some symbol could not be expanded -- cannot happen since its last rule is a 'default' selection
            # (ii) all expansions are done
            # (iii) there are valid expansions left to be done.
            # If the expression is unchanged, return the value as there are no more symbols to be expanded. 
            if expr == expanded_expr:
                return expr
            else:
                # Recursively apply valuation on the expanded expression
                return evaluate_aux(expanded_expr)

        # Call the auxiliary function and return the result
        return evaluate_aux()

    def pretty_smt_encoding(self):
        """
        Return a string in SMT-Lib format that (i) Declares variables and (ii) an evaluation function corresponding 
        to the grammar. Refer to the package and module descriptions for the roles and intended meaning 
        of these commands.  
        :return: string  
        """
        # TODO (high): construct lisplike.is_lisplike values instead of strings
        # Precomputing useful values
        synthfun_name = self.sygus_grammar.get_name()
        typed_nonterminals = dict(self.sygus_grammar.get_typed_nonterminal_list())
        typed_params = [[arg, smt_type] for (arg, smt_type) in self.sygus_grammar.get_typed_parameter_list()]
        # Degenerates to '()' when the list of arguments is empty
        typed_param_string = lisplike.pretty_string(typed_params, noindent=True)
        arguments = [arg[0] for arg in typed_params]
        ordered_rule_dict = self.sygus_grammar.get_ordered_rule_list()
        define_fun_format = '(define-fun {name} {typed_args} {return_type}\n{body}\n)\n'
        # Declare boolean variables
        # TODO (medium): refactor code to have each variable with its type. Only boolean variables currently
        boolvar_decls = '\n'.join(['(declare-const {} Bool)'.format(boolvar) for boolvar in self.boolvars])
        bool_decl_string = '\n;Declaring boolean variables to encode grammar\n{}'.format(boolvar_decls)
        # Define functions for each nonterminal copy grouped by the original nonterminal
        func_decl_string = ';Declaring functions corresponding to nonterminals\n'
        for nonterminal in self.sygus_grammar.get_ordered_nonterminal_list():
            func_decl_string = func_decl_string + ';Functions corresponding to {}\n'.format(nonterminal)
            return_type = typed_nonterminals[nonterminal]
            return_type_string = lisplike.pretty_string(return_type, noindent=True)
            post_nonterminals = self._post[nonterminal]
            nonterminal_copies = [nt_copy for nt_copy in self.symbols if self.symbols[nt_copy][0] == nonterminal]
            for nonterminal_copy in nonterminal_copies:
                choice_boolvars = self.symbols[nonterminal_copy][1]
                post_nonterminal_copies = [self.boolvars[choice_boolvar] for choice_boolvar in choice_boolvars]
                # Include catch case
                post_nonterminal_copies.append(self.boolcatch[nonterminal_copy])
                if arguments != []:
                    # If there are arguments, each of the nonterminal copies will need to appear in the form of 
                    # applications to the arguments.
                    post_nonterminal_copies_with_args = [[[nt_copy] + arguments 
                                                          for nt_copy in nt_copy_list] 
                                                         for nt_copy_list in post_nonterminal_copies]
                else:
                    post_nonterminal_copies_with_args = post_nonterminal_copies
                # Compute the expansion rules with nonterminal copies and arguments in place of the nonterminals
                substituted_expansions = [lisplike.substitute(ordered_rule_dict[nonterminal][i],
                                                              list(zip(post_nonterminals[i],
                                                                       post_nonterminal_copies_with_args[i])))
                                          for i in range(len(ordered_rule_dict[nonterminal]))]

                # Auxiliary function
                def func_decl_body_aux(boolvars, rules):
                    # New version of auxiliary function to use ite statements only when choice of rules remains.
                    # Hack around lisplike pretty printer's lack of customization.
                    # Putting \n and pretty printing with 'no indent' as a manner of controlling indentation.
                    # TODO (medium): Eliminate explicit construction of lisplike representations
                    if len(rules) == 1:
                        # Base case with single rule; simply apply the replacement
                        # Boolvars should be [] in this case
                        return rules[0]
                    else:
                        # Structure an ite operator on first boolvar/rule, then recurse
                        return ['ite', boolvars[0], '\n', rules[0], '\n', func_decl_body_aux(boolvars[1:], rules[1:])]

                func_body = lisplike.pretty_string(func_decl_body_aux(choice_boolvars, substituted_expansions), 
                                                   noindent=True)
                func_decl = define_fun_format.format(name=nonterminal_copy, typed_args=typed_param_string, 
                                                     return_type=return_type_string, body=func_body)
                func_decl_string = func_decl_string + func_decl
        # Define the replacement for the synth-fun command
        # Must have the same name as the function to be synthesised
        synthfun_return_type = self.sygus_grammar.get_range_type()
        synthfun_return_type_string = lisplike.pretty_string(synthfun_return_type, noindent=True)
        starting_symbol = self.starting_symbol
        evalfun_body = '({} {})'.format(starting_symbol, ' '.join(arguments)) if arguments != [] else starting_symbol
        eval_function_string = (';Function to be synthesised\n' + define_fun_format).format(
            name=synthfun_name, typed_args=typed_param_string, 
            return_type=synthfun_return_type_string, body=evalfun_body)
        # Return the boolean declarations, function declarations, and the eval function
        return bool_decl_string + '\n\n' + func_decl_string + '\n' + eval_function_string

    def get_synth_function(self, valuation=None):
        """
        The synthesized function part of pretty_smt_encoding.
        :param valuation: dict {string: bool}
        :return synth_function_string: string
        """
        # TODO (medium): simplify with pretty_smt_encoding
        define_fun_format = '(define-fun {name} {typed_args} {return_type}\n{body}\n)\n'
        synthfun_name = self.sygus_grammar.get_name()
        synthfun_return_type = self.sygus_grammar.get_range_type()
        starting_symbol = self.starting_symbol
        typed_params = [[arg, smt_type] for (arg, smt_type) in self.sygus_grammar.get_typed_parameter_list()]
        arguments = [arg[0] for arg in typed_params]
        typed_param_string = lisplike.pretty_string(typed_params, noindent=True)
        if valuation is None:
            synthfun_body = '({} {})'.format(starting_symbol, ' '.join(arguments)) if arguments != [] else starting_symbol
        else:
            synthfun_body = lisplike.pretty_string(self.evaluate(valuation), noindent=True)
        synth_function_string = (define_fun_format).format(
            name=synthfun_name, typed_args=typed_param_string, 
            return_type=synthfun_return_type, body=synthfun_body)
        return synth_function_string


# Helper functions
def _nonterminal_copy_name(symbol_name, copy_number, synthfun_name):
    return '{}_{}_{}'.format(synthfun_name, symbol_name, copy_number)


def _boolvar_name(boolvar_number, synthfun_name):
    return '{}_b{}'.format(synthfun_name, boolvar_number)
