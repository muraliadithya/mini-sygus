"""
Module with a single class 'SMTGrammar'.  
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
as such obejcts of this implementation of the SMTGrammar class can only be those corresponding to finite grammars. 
Lastly, each occurrence of a nonterminal anywhere in this structure is renamed to a unique symbol. Note that the 
construction is completely agnostic to the types of the nonterminals.  

The tree-like structure then represents the total relationship between nonterminals and expansions for any possible 
yield of the grammar, where a particular yield corresponds to the values of all the aforementioned boolean variables. 
This relationship can be presented in the form of a constraint to an SMT solver, which achieves component (ii) 
above.  
"""

from src.SyGuSGrammar import track_nonterminals_one_step, SyGuSGrammar


class SMTGrammar:
    """
    Basic class that generates a constraint-based representation of a SyGuS grammar. 
    """
    def __init__(self, sygus_grammar):
        if not isinstance(sygus_grammar, SyGuSGrammar):
            raise TypeError('Initialise SMTGrammar object with a corresponding SyGuSGrammar object.')
        elif not sygus_grammar.is_finite():
            raise ValueError('Grammar is not finite. Unsupported.')
        # Preprocessing
        nonterminals = {typed_nonterminal[0] for typed_nonterminal in sygus_grammar.get_typed_nonterminal_set()}

        # Essential attributes
        self.sygus_grammar = sygus_grammar
        # Dictionary of boolean variables representing choices of rules for various copies of nonterminals.
        # Each boolean variable points to a unique expansion rule for some nonterminal in the grammar.
        # Keys are the names of the boolean variables as strings. Values are a list of strings.
        # The list is of names of nonterminal copies corresponding to the actual nonterminals in the production rule 
        # pointed to by the boolean variable. The order of the copies is the order in which the nonterminals appear 
        # in the sygus_grammar._post dictionary.
        self.boolvars = dict()
        # Dictionary of copies of nonterminals.
        # The keys are the names of the copies as strings. Values are a tuple (parent, list of boolvars)
        # Parent is the original nonterminal for which the key is a copy, and the list is of boolean variables 
        # corresponding to the choice of each production rule.
        # The order of boolvars is the order in which the rules appear in the ordered_rule_dict.
        self.symbols = dict()

        # Internal attributes (should not exposed by any methods)
        self._nonterminal_copy_counter = {nonterminal: 0 for nonterminal in nonterminals}
        if sygus_grammar._post is None:
            sygus_grammar._post = track_nonterminals_one_step(sygus_grammar)

        # Attributes for caching useful values
        # self._post = sygus_grammar._post
