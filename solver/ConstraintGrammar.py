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

from solver.SyGuSGrammar import track_nonterminals_one_step, SyGuSGrammar
import solver.lisplike as lisplike


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
        if not sygus_grammar.is_terminable():
            raise ValueError('Grammar contains rule sets which are exclusively self-referential and not supported.')
        # Preprocessing
        # nonterminals = sygus_grammar.get_nonterminal_set()

        # Essential attributes
        self.sygus_grammar = sygus_grammar
        # Dictionary of boolean variables representing choices of rules for various copies of nonterminals.
        # Each boolean variable points to a unique expansion rule for some nonterminal in the grammar.
        # Keys are the names of the boolean variables as strings. Values are a list of strings.
        # The list is of names of nonterminal copies corresponding to the actual nonterminals in the production rule 
        # pointed to by the boolean variable. The order of the copies is the order in which the nonterminals appear 
        # in the SyGuSGrammar.post dictionary.
        self.boolvars = None
        # Dictionary similar to self.boolvars representing the catch case of the final replacement rule choice.
        # Keys are the names of nonterminal copies whose catch case is contained in the value.
        # Values are the names of nonterminal copies corresponding to the actual nonterminals in the (final)
        # production rule for the nonterminal copy key.
        self.boolcatch = None
        # Dictionary of copies of nonterminals.
        # The keys are the names of the copies as strings. Values are a tuple (parent, list of boolvars)
        # Parent is the original nonterminal for which the key is a copy, and the list is of boolean variables 
        # corresponding to the choice of each production rule. The order of boolvars is the order in which 
        # the rules appear in the result of SyGuSGrammar.get_ordered_rule_dict.
        self.symbols = None
        # Dictionary of copies of exceptional nonterminals (regarding maximum depth of grammar expansion).
        # The keys are the names of the copies as strings, if rules were excluded due to lack of viability
        # from max_depth parameter in the constraint encoding. Each value is a list of rule indices which are viable.
        self.rulecatch = None
        # Starting symbol to traverse the constraint-based representation
        self.starting_symbol = None

        # Internal attributes (should not exposed by any methods)
        self._post = track_nonterminals_one_step(sygus_grammar)
        self._rule_dict = sygus_grammar.get_ordered_rule_list()

        # Attributes for caching useful values
        # self.post = track_nonterminals_one_step(sygus_grammar)

    def compute_constraint_encoding(self, max_depth=None):
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
        self.rulecatch = dict()
        # Counter for creating fresh boolean variable names
        boolcounter = 0
        self.symbols = dict()
        start_symbol = self.sygus_grammar.get_start_symbol()
        # Counters for creating fresh nonterminal copy names
        nonterminal_copy_counter = {nonterminal: 0 for nonterminal in self.sygus_grammar.get_nonterminal_set()}
        synthfun_name = self.sygus_grammar.get_name()

        # Ensure max_depth allows for some admissible string
        least_heights = self.sygus_grammar.get_nonterminal_heights(least=True)
        if max_depth is not None and max_depth < least_heights[start_symbol]:
            raise ValueError('Insufficient grammar depth.')
            # max_depth = least_heights[start_symbol]
        # Worklist algorithm to compute self.boolvars and self.symbols such that they are populated with the 
        # intended meaning. Refer to the extensive comments in the __init__ function for what these variables 
        # should contain.
        # Worklist will contain pairs (nonterminal, nonterminal_copy). Initial pair is the start symbol and its copy.
        start_symbol_initial_copy = _nonterminal_copy_name(start_symbol,
                                                           nonterminal_copy_counter[start_symbol],
                                                           synthfun_name)
        self.starting_symbol = start_symbol_initial_copy
        nonterminal_copy_counter[start_symbol] = nonterminal_copy_counter[start_symbol] + 1

        worklist = {1: {(start_symbol, start_symbol_initial_copy)}}
        depth = 1
        while worklist[depth]:
            nonterminal, nonterminal_copy = worklist[depth].pop()
            # Invent as many new boolean variables as rules (minus one), and add the entry to symbols
            # Accept only rules which will lead to admissible strings within max_depth
            if max_depth is not None:
                valid_ind = [i for i, rule in enumerate(self._rule_dict[nonterminal]) if
                             max([0]+[least_heights[sym] for sym in self._post[nonterminal][i]]) <= max_depth-depth]
                rule_list = [self._rule_dict[nonterminal][i] for i in valid_ind]
            else:
                valid_ind = list(range(len(self._rule_dict[nonterminal])))
                rule_list = self._rule_dict[nonterminal]
            num_rules = len(rule_list)
            if num_rules < len(self._rule_dict[nonterminal]):
                # If rules were excluded due to foresight toward max_depth, store the valid rule indices
                self.rulecatch[nonterminal_copy] = valid_ind
            new_boolvars = []
            # Need one fewer boolean variables than the number of valid rules
            for _ in range(num_rules-1):
                fresh_boolvar_number = boolcounter
                fresh_boolvar_name = _boolvar_name(fresh_boolvar_number, synthfun_name)
                boolcounter = boolcounter + 1
                new_boolvars = new_boolvars + [fresh_boolvar_name]
            self.symbols[nonterminal_copy] = (nonterminal, new_boolvars)
            # For each rule create new nonterminal copies and add the entry to boolvars.
            for i in range(num_rules):
                post_symbols = self._post[nonterminal][valid_ind[i]]
                post_symbol_copies = []
                for symbol in post_symbols:
                    fresh_nonterminal_number = nonterminal_copy_counter[symbol]
                    fresh_nonterminal_name = _nonterminal_copy_name(symbol, fresh_nonterminal_number, synthfun_name)
                    nonterminal_copy_counter[symbol] = nonterminal_copy_counter[symbol] + 1
                    post_symbol_copies = post_symbol_copies + [fresh_nonterminal_name]
                    # Add the copies with the original symbols to the worklist.
                    if max_depth is None or depth < max_depth:
                        try:
                            worklist[depth+1].add((symbol, fresh_nonterminal_name))
                        except Exception:
                            worklist[depth+1] = {(symbol, fresh_nonterminal_name)}
                if i < num_rules-1:
                    boolvar_name = new_boolvars[i]
                    self.boolvars[boolvar_name] = post_symbol_copies
                else:
                    # Catchall case for symbol copies of last production rule
                    # Same as the entry in the if branch but made in self.boolcatch
                    self.boolcatch[nonterminal_copy] = post_symbol_copies

            # Increase depth if current depth is exhausted and next depth has work.
            if not worklist[depth] and depth+1 in worklist:
                depth += 1

    def evaluate(self, valuation):
        """
        Apply the given valuation on boolean variables to the representation. The result is an expression from 
        the grammar.  
        :param valuation: dict {string: bool}  
        :return: lisplike.is_lisplike
        """
        # TODO (medium-high): rewrite evaluate entirely to use minimised valuations from minimise_valuation. 
        # That way one does not need to check that all boolean variables have a valuation that is boolean.
        if not set(self.boolvars.keys()).issubset(set(valuation.keys())):
            remaining_boolvars = set(self.boolvars.keys()) - set(valuation.keys())
            raise NonsenseValuationException('The given valuation does not interpret '
                                             'the following boolean variables: {}'.format(remaining_boolvars))
        elif not all(isinstance(valuation[boolvar], bool) for boolvar in self.boolvars):
            raise NonsenseValuationException('Variables must have a boolean valuation.')
        ordered_rule_dict = self._rule_dict
        starting_symbol = self.starting_symbol
        # Construct pairs containing each symbol and the expression it expands to based on the valuation
        substitution_pairs = []
        for symbol in self.symbols:
            original_symbol, rule_choice_boolvars = self.symbols[symbol]
            try:
                # Identify first boolvar which is True
                chosen_rule_index = next(i for i, boolvar in enumerate(rule_choice_boolvars)
                                         if valuation[boolvar])
                nonterminal_copies = self.boolvars[rule_choice_boolvars[chosen_rule_index]]
            except StopIteration:
                # Boolvars are all False; execute the catch case
                # Select the last valid expansion rule
                chosen_rule_index = -1
                nonterminal_copies = self.boolcatch[symbol]
            if symbol in self.rulecatch:
                # If ruleset is exceptional, adjust index accordingly
                chosen_rule_index = self.rulecatch[symbol][chosen_rule_index]
            chosen_rule = ordered_rule_dict[original_symbol][chosen_rule_index]
            nonterminals_in_rule = self._post[original_symbol][chosen_rule_index]

            # Hack around lisplike.transform by using a single transformation that substitutes pairs only once
            nonterminal_copy_pairs = list(zip(nonterminals_in_rule, nonterminal_copies))

            # Auxiliary function to compute the hack transform
            # Second argument is mutable on purpose in order to retain memory between calls
            def _nonterminal_copy_substitute(expr, copy_pairs=nonterminal_copy_pairs):
                for (nonterminal, nonterminal_copy) in copy_pairs:
                    if expr == nonterminal:
                        copy_pairs.remove((nonterminal, nonterminal_copy))
                        return nonterminal_copy
                # No matching substitutions. Return original expression
                return expr
            # Compute the rule expansions with nonterminal copies using lisplike.transform
            # NOTE: IMPORTANT: the postorder traversal makes the substitutions deterministic and in accordance with 
            # the encoding returned by pretty_smt_encoding
            substitution = lisplike.transform(chosen_rule, 
                                              [(lambda x: True, lambda x: _nonterminal_copy_substitute(x))],
                                              traversal_order='postorder')
            substitution_pairs = substitution_pairs + [(symbol, substitution)]

        # Auxiliary function to apply valuations and build the result recursively
        def evaluate_aux(expr=None):
            if expr is None:
                expr = starting_symbol
            # If there are any nonterminals in the expression substitute them with the expansion rules recursively
            expanded_expr = lisplike.substitute(expr, substitution_pairs)
            # There are only three choices: 
            # (i) some symbol could not be expanded -- should not happen since its last rule is a 'default' selection
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

        # Auxiliary function to compute function declaration of a particular nonterminal copy.
        def aux_func_declare(nonterminal_copy):
            nonterminal, choice_boolvars = self.symbols[nonterminal_copy]
            # Aggregate dependent nonterminal copies
            dependents = set().union(*[self.boolvars[choice_boolvar] for choice_boolvar in choice_boolvars])
            if nonterminal_copy in self.boolcatch:
                dependents.update(self.boolcatch[nonterminal_copy])
            return_type = typed_nonterminals[nonterminal]
            return_type_string = lisplike.pretty_string(return_type, noindent=True)
            post_nonterminal_copies = [self.boolvars[choice_boolvar] for choice_boolvar in choice_boolvars]
            if nonterminal_copy in self.rulecatch:
                post_nonterminals = [self._post[nonterminal][i] for i in self.rulecatch[nonterminal_copy]]
            else:
                post_nonterminals = self._post[nonterminal]
            # Include catch case
            if nonterminal_copy in self.boolcatch:
                post_nonterminal_copies.append(self.boolcatch[nonterminal_copy])
            if arguments != []:
                # If there are arguments, each of the nonterminal copies will need to appear in the form of 
                # applications to the arguments.
                post_nonterminal_copies_with_args = [[[nt_copy] + arguments 
                                                      for nt_copy in nt_copy_list] 
                                                     for nt_copy_list in post_nonterminal_copies]
            else:
                post_nonterminal_copies_with_args = post_nonterminal_copies
            # Determine the appropriate rule list for nonterminal copy.
            if nonterminal_copy in self.rulecatch:
                rule_list = [ordered_rule_dict[nonterminal][i] for i in self.rulecatch[nonterminal_copy]]
            else:
                rule_list = ordered_rule_dict[nonterminal]
            # If no valid rules are available, no need to write the corresponding function.
            if len(rule_list) == 0:
                return '', set()
            # Begin replacement
            substituted_expansions = []
            for i in range(len(rule_list)):
                # Hack around lisplike.transform by using a single transformation that substitutes pairs only once
                nonterminal_copy_with_arg_pairs = list(zip(post_nonterminals[i], 
                                                           post_nonterminal_copies_with_args[i]))

                # Auxiliary function to compute the hack transform
                # Second argument is mutable on purpose in order to retain memory between calls
                def _nonterminal_copy_substitute(expr, copy_pairs=nonterminal_copy_with_arg_pairs):
                    for (nt, nt_copy_with_arg) in copy_pairs:
                        if expr == nt:
                            copy_pairs.remove((nt, nt_copy_with_arg))
                            return nt_copy_with_arg
                    # No matching substitutions. Return original expression
                    return expr

                # Add the transformed rule to substituted_expansions
                # NOTE: IMPORTANT: The postorder traversal fixes the substitutions in a deterministic way 
                # that can be recovered while evaluating valuations from the solver ot get yields from the 
                # grammar. Check that the evaluate function uses/maintains this order.
                transformed_rule = lisplike.transform(rule_list[i], 
                                                      [(lambda x: True, 
                                                        lambda x: _nonterminal_copy_substitute(x))], 
                                                      traversal_order='postorder')
                substituted_expansions.append(transformed_rule)

            # Auxiliary function for computing the body of a function declaration
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
            return func_decl, dependents

        # Construct function declarations
        if self.sygus_grammar.is_finite():
            # Define functions for each nonterminal copy grouped by the original nonterminal.
            # This ordering is well-defined for finite grammars.
            func_decl_string = ';Declaring functions corresponding to nonterminals\n'
            for nonterminal in self.sygus_grammar.get_ordered_nonterminal_list():
                func_decl_string = func_decl_string + ';Functions corresponding to {}\n'.format(nonterminal)
                for nonterminal_copy in self.symbols:
                    # Only move forward with copies whose parent is the nonterminal at hand
                    if self.symbols[nonterminal_copy][0] != nonterminal:
                        continue
                    func_decl, _ = aux_func_declare(nonterminal_copy)
                    func_decl_string += func_decl
        else:
            # If grammar is infinite, printed order must depend on nonterminal copy dependence,
            # since there is no longer a linear ordering on the nonterminal symbols themselves.
            func_decl_string = ''
            worklist = {self.starting_symbol}
            while worklist:
                nonterminal_copy = worklist.pop()
                func_decl, dependents = aux_func_declare(nonterminal_copy)
                worklist.update(dependents)
                # Function declarations must be in reverse order of dependence
                func_decl_string = func_decl + func_decl_string
            func_decl_string = ';Declaring functions corresponding to nonterminals\n' + func_decl_string

        # Define the replacement for the synth-fun command
        # Must have the same name as the function to be synthesised
        synthfun_return_type = self.sygus_grammar.get_range_type()
        synthfun_return_type_string = lisplike.pretty_string(synthfun_return_type, noindent=True)
        starting_symbol = self.starting_symbol
        evalfun_body = '({} {})'.format(starting_symbol, ' '.join(arguments)) if arguments != [] else starting_symbol
        eval_function_string = ';Function to be synthesised\n' + _definefun_command(
            synthfun_name, typed_param_string, synthfun_return_type_string, evalfun_body)
        # Return the boolean declarations, function declarations, and the eval function
        return bool_decl_string + '\n\n' + func_decl_string + '\n' + eval_function_string

    # TODO (medium-high): generalise function to minimise valuation and evaluate 
    #  the yield simultaneously and get rid of evaluate
    def minimise_valuation(self, valuation):
        """
        Return a minimised valuation such that the values of variables not appearing in the dictionary 
        do not influence the satisfiability of constraints.  
        Used to determine the specific boolean variables among those in the given valuation that indicate 
        the synthesis result. Refer to the module description to understand the encoding and why 
        only some variables might be essential.  
        :param valuation: dict {string: bool}  
        """
        # Eliminate keys that are not present in boolvars
        valuation = {k: v for k, v in valuation.items() if k in self.boolvars}
        # Check that all values are boolean
        # Using a worklist follow nonterminal copies and look at the boolean variables 
        # corresponding to them in the order present in self.symbols until one of them is true.
        # If all of them are present but none of them have their valuation as True, then all the variables 
        # are relevant.
        worklist = {self.starting_symbol}
        relevant_boolvars = set()
        while worklist:
            nonterminal_copy = worklist.pop()
            boolvars_for_nt_copy = self.symbols[nonterminal_copy][1]
            boolvar_index = 0
            while boolvar_index < len(boolvars_for_nt_copy):
                try:
                    boolvar_valuation = valuation[boolvars_for_nt_copy[boolvar_index]]
                    if isinstance(boolvar_valuation, bool):
                        if boolvar_valuation:
                            # Boolean variable is true. Rule chosen.
                            break
                    else:
                        raise NonsenseValuationException('Given valuation is not sensible: value of {} must be '
                                                         'boolean.'.format(boolvars_for_nt_copy[boolvar_index]))
                except KeyError:
                    raise NonsenseValuationException('Given valuation is not sensible: '
                                                     'value of {} needed'.format(boolvars_for_nt_copy[boolvar_index]))
                boolvar_index = boolvar_index + 1
            # End of loop. All boolvars until and including boolvar_index are relevant.
            relevant_boolvars.update(boolvars_for_nt_copy[:boolvar_index+1])
            # Update worklist with all the nonterminal copies belonging to the chosen rule.
            # The index of the chosen rule is the same as boolvar_index
            # Case-split depending on whether the copies will be in self.boolvars or self.boolcatch
            if boolvar_index == len(boolvars_for_nt_copy):
                worklist.update(self.boolcatch[nonterminal_copy])
            else:
                worklist.update(self.boolvars[boolvars_for_nt_copy[boolvar_index]])
        return {boolvar: valuation[boolvar] for boolvar in relevant_boolvars}

    def valuation_to_definefun_command(self, valuation):
        """
        Pretty printer for displaying the result of synthesis.  
        The given valuation is converted into a define-fun command that is in SMT-Lib format.  
        :param valuation: dict {string: bool}  
        :return: string  
        """
        synthfun_name = self.sygus_grammar.get_name()
        typed_params = [[arg, smt_type] for (arg, smt_type) in self.sygus_grammar.get_typed_parameter_list()]
        synthfun_typed_args = lisplike.pretty_string(typed_params, noindent=True)
        synthfun_return_type = lisplike.pretty_string(self.sygus_grammar.get_range_type(), noindent=True)
        synthfun_body = lisplike.pretty_string(self.evaluate(valuation), noindent=True)
        return _definefun_command(synthfun_name, synthfun_typed_args, synthfun_return_type, synthfun_body)

    def proposal_to_definefun_command(self, proposal):
        """
        Pretty printer for displaying a proposed solution to synthesis.
        The given proposal is wrapped into a define-fun command that is in SMT-Lib format.
        :param proposal: string
        :return: string
        """
        propfun_name = self.sygus_grammar.get_name()
        typed_params = [[arg, smt_type] for (arg, smt_type) in self.sygus_grammar.get_typed_parameter_list()]
        propfun_typed_args = lisplike.pretty_string(typed_params, noindent=True)
        propfun_return_type = lisplike.pretty_string(self.sygus_grammar.get_range_type(), noindent=True)
        propfun_body = proposal
        return _definefun_command(propfun_name, propfun_typed_args, propfun_return_type, propfun_body)


# Helper functions
def _definefun_command(name, typed_args, return_type, body):
    definefun_format = '(define-fun {name} {typed_args} {return_type}\n{body}\n)\n'
    definefun_string = definefun_format.format(name=name, typed_args=typed_args,
                                               return_type=return_type, body=body)
    return definefun_string


def _nonterminal_copy_name(symbol_name, copy_number, synthfun_name):
    return '{}_{}_{}'.format(synthfun_name, symbol_name, copy_number)


def _boolvar_name(boolvar_number, synthfun_name):
    return '{}_b{}'.format(synthfun_name, boolvar_number)
