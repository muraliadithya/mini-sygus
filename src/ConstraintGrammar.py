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
        self._nonterminals = nonterminals
        self._rule_dict = sygus_grammar.get_ordered_rule_list()
        # Special symbol to denote when no rule is chosen for a symbol according to valuation
        self._no_rule_chosen = '||NoRuleChosen||'

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
        # Counter for creating fresh boolean variable names
        boolcounter = 0
        self.symbols = dict()
        start_symbol = self.sygus_grammar.get_start_symbol()
        # Counters for creating fresh nonterminal copy names
        nonterminal_copy_counter = {nonterminal: 0 for nonterminal in self._nonterminals}
        synthfun_name = self.sygus_grammar.get_name()

        # Worklist algorithm to compute self.boolvars and self.symbols such that they are populated with the 
        # intended meaning. Refer to the extensive comments in the __init__ function for what these variables 
        # should contain.
        # Worklist will contain pairs (nonterminal, nonterminal_copy). Initial pair is the start symbol and a copy.
        start_symbol_initial_copy = _nonterminal_copy_name(start_symbol, nonterminal_copy_counter[start_symbol], synthfun_name)
        self.starting_symbol = start_symbol_initial_copy
        nonterminal_copy_counter[start_symbol] = nonterminal_copy_counter[start_symbol] + 1
        worklist = {(start_symbol, start_symbol_initial_copy)}
        while worklist:
            nonterminal, nonterminal_copy = worklist.pop()
            # Invent as many new boolean variables as rules, and add the entry to symbols
            rule_list = self._rule_dict[nonterminal]
            num_rules = len(rule_list)
            new_boolvars = []
            for _ in range(num_rules):
                fresh_boolvar_number = boolcounter
                fresh_boolvar_name = _boolvar_name(fresh_boolvar_number, synthfun_name)
                boolcounter = boolcounter + 1
                new_boolvars = new_boolvars + [fresh_boolvar_name]
            self.symbols[nonterminal_copy] = (nonterminal, new_boolvars)

            # For each rule create new nonterminal copies and add the entry to boolvars. 
            for i in range(num_rules):
                boolvar_name = new_boolvars[i]
                post_symbols = self._post[nonterminal][i]
                post_symbol_copies = []
                for symbol in post_symbols:
                    fresh_nonterminal_number = nonterminal_copy_counter[symbol]
                    fresh_nonterminal_name = _nonterminal_copy_name(symbol, fresh_nonterminal_number, synthfun_name)
                    nonterminal_copy_counter[symbol] = nonterminal_copy_counter[symbol] + 1
                    post_symbol_copies = post_symbol_copies + [fresh_nonterminal_name]
                    # Add the copies with the original symbols to the worklist.
                    worklist.add((symbol, fresh_nonterminal_name))
                self.boolvars[boolvar_name] = post_symbol_copies

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
        valuation_pairs = []
        for symbol in self.symbols:
            original_symbol, rule_choice_boolvars = self.symbols[symbol]
            try:
                chosen_rule_index = next(i for i in range(len(rule_choice_boolvars)) if valuation[rule_choice_boolvars[i]])
                chosen_rule = ordered_rule_dict[original_symbol][chosen_rule_index]
                # Substitute the occurrences of nonterminals in the rule with their copies for further evaluation
                # Order of boolvars and _post have been coordinated with the order of the rules. Refer __init__.
                nonterminals_in_rule = self._post[original_symbol][chosen_rule_index]
                nonterminal_copies = self.boolvars[rule_choice_boolvars[chosen_rule_index]]
                substitution = lisplike.substitute(chosen_rule, list(zip(nonterminals_in_rule, nonterminal_copies)))
            except StopIteration:
                # No rule is chosen according to the valuation.
                # chosen_rule_index = None
                # chosen_rule = self._no_rule_chosen
                substitution = self._no_rule_chosen
            # If no rule is chosen, write a special symbol.
            valuation_pairs = valuation_pairs + [(symbol, substitution)]

        # Auxiliary function to apply valuations and build the result recursively
        def evaluate_aux(expr=None):
            if expr is None:
                expr = starting_symbol
            # If there are any nonterminals in the expression substitute them with the expansion rules recursively
            expanded_expr = lisplike.substitute(expr, valuation_pairs)
            # There are only three choices: 
            # (i) some symbol could not be expanded to anything
            # (ii) all expansions are done
            # (iii) there are valid expansions left to be done.
            # If any symbol is expanded such that the no rule chosen symbol appears, then stop and raise exception
            if lisplike.is_subexpr(self._no_rule_chosen, expanded_expr):
                # TODO (medium-low): output the symbol/path within the grammar where the valuation does not make sense.
                raise NonsenseValuationException('The given valuation does not make sense.')
            # If the expression is unchanged, return the value as there are no more symbols to be expanded. 
            if expr == expanded_expr:
                return expr
            else:
                # Recursively apply valuation on the expanded expression
                return evaluate_aux(expanded_expr)

        # Call the auxiliary function and return the result
        return evaluate_aux()


# Helper functions
def _nonterminal_copy_name(symbol_name, copy_number, synthfun_name):
    return '{}_{}_{}'.format(synthfun_name, symbol_name, copy_number)


def _boolvar_name(boolvar_number, synthfun_name):
    return '{}_b{}'.format(synthfun_name, boolvar_number)
