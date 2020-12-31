import src.lisplike as lisplike


# NOTE: Some argument/output types are written as lisplike.is_lisplike_repr. This is currently enforced nowhere.
# Need to provide tighter integration with lisplike data types and checking in a way that can be clearly inferred.
class SyGuSGrammar:
    """
    Class representing arguments to a synth-fun command (refer SyGuS 2.0 format: https://sygus.org/language/).  
    Attribute variables are explained in the documentation for the respective getter functions.  
    """

    def __init__(self):
        # Attributes defining the function to be synthesised
        self.name = None
        self.parameters = None
        self.range_type = None

        # Attributes defining the grammar
        self.nonterminals = dict()
        self.start_symbol = None
        self.rules = dict()

        # Attributes for caching useful values
        # Dictionary of nonterminals produced post the expansion of a rule from a given nonterminal
        self._post = None

    def name_synth_fun(self, name):
        """
        Name of the function to be synthesised.  
        :param name: string  
        """
        self.name = name

    def specify_parameters(self, typed_params_list):
        """
        Ordered list of input parameter names and types for the synthesised function.  
        :param typed_params_list: list of (string, lisplike.is_lisplike_repr)  
        """
        self.parameters = dict()
        for typed_param in typed_params_list:
            param_name, smt_type = typed_param
            if param_name in self.parameters:
                raise ValueError('Redeclaration of parameter {}'.format(param_name))
            self.parameters[param_name] = smt_type

    def define_range(self, smt_type):
        """
        Range of the synthesised function.  
        :param smt_type: lisplike.is_lisplike_repr  
        """
        self.range_type = smt_type

    def add_nonterminal(self, nonterminal, smt_type):
        """
        Nonterminal in the grammar.  
        :param nonterminal: string  
        :param smt_type: lisplike.is_lisplike_repr  
        """
        if nonterminal in self.nonterminals and smt_type != self.nonterminals[nonterminal]:
            raise ValueError(
                'Nonterminal {} already declared with type {}.'.format(nonterminal, self.nonterminals[nonterminal]))
        self.nonterminals[nonterminal] = smt_type

    def add_nonterminals(self, typed_nonterminals_list):
        """
        Nonterminals in the grammar. The first nonterminal in the list is assumed to be the start symbol if one 
        is not defined already.  
        :param typed_nonterminals_list: list of (string, lisplike.is_lisplike_repr)  
        """
        for typed_nonterminal in typed_nonterminals_list:
            nonterminal, smt_type = typed_nonterminal
            self.add_nonterminal(nonterminal, smt_type)
        if self.start_symbol is None and typed_nonterminals_list != []:
            self.add_start_symbol(typed_nonterminals_list[0][0])

    def add_start_symbol(self, start_symbol_name):
        """
        Name of starting nonterminal from which productions will be considered for synthesis.  
        :param start_symbol_name: string  
        """
        if start_symbol_name not in self.nonterminals:
            raise ValueError('{} is not a valid nonterminal'.format(start_symbol_name))
        current_start_symbol = self.start_symbol
        if current_start_symbol is not None and start_symbol_name != current_start_symbol:
            raise ValueError('{} already declared as the start symbol.'.format(current_start_symbol))
        self.start_symbol = start_symbol_name

    def add_rule(self, nonterminal, rule):
        """
        Add a production rule for a nonterminal.  
        :param nonterminal: string  
        :param rule: lisplike.is_lisplike_repr  
        """
        # TODO (medium): store rules for each nonterminal not in a list, but indexed by some name in order 
        #  to correspond and track rules to rule-specific attributes (such as the occurrence of a particular symbol)
        if nonterminal not in self.rules:
            self.rules[nonterminal] = []
        self.rules[nonterminal].append(rule)

    def get_name(self):
        """
        Return name of the function to be synthesised.  
        :return: string  
        """
        return self.name

    def get_typed_parameter_list(self):
        """
        Return list of input parameter names and types for the synthesised function. The order of elements in the 
        list is the same as the order of parameters.    
        :return: list of (string, lisplike.is_lisplike_repr)  
        """
        return self.parameters

    def get_range_type(self):
        """
        Return the range of the function to be synthesised as an smt type in lisp-like representation.  
        :return: lisplike.is_lisplike_repr  
        """
        return self.range_type

    def get_typed_nonterminal_set(self):
        """
        Return the set of nonterminals in the grammar with their types.  
        :return: list of (string, lisplike.is_lisplike_repr)  
        """
        return set((nonterminal, self.nonterminals[nonterminal]) for nonterminal in self.nonterminals)

    def get_start_symbol(self):
        """
        Return the start symbol among the nonterminals.  
        :return: string  
        """
        return self.start_symbol

    def get_ordered_rule_list(self, *nonterminals):
        """
        Return the list of production rules for the given nonterminals in a dictionary indexed by the nonterminals.  
        The list is ordered deterministically. If no nonterminals are specified, then the rule list is returned for 
        all possible nonterminals.  
        :param nonterminals: sequence of string   
        :return: dict {string: list of lisplike.is_lisplike_repr}  
        """
        nonterminals = list(nonterminals)
        if not nonterminals:
            # No nonterminals specified
            nonterminals = self.nonterminals.keys()
        return {nonterminal: sorted(self.rules[nonterminal]) for nonterminal in nonterminals}

    def is_finite(self):
        """
        Check whether the grammar only has finite productions.  
        A grammar has an infinite production if there is a sequence of nonterminals B_1, B_2, ... B_n 
        such that B_i has a rule that contains B_i+1 in its expansion, and B_n contains B_1.  
        :return: bool  
        """
        # Compute the set of nonterminals that occur in each production rule for each nonterminal.
        # See if the relevant caching attribute holds a valid value
        if self._post is None:
            self._post = track_nonterminals_one_step(self)
        ordered_post_dict = self._post
        worklist = {self.get_start_symbol()}
        seen_nonterminals = worklist
        while worklist:
            nonterminal = worklist.pop()
            if nonterminal in seen_nonterminals:
                return False
            worklist.union({symbol for symbols_in_rule in ordered_post_dict[nonterminal] for symbol in symbols_in_rule})
        # Entire grammar has been traversed without a cycle. Grammar is finite.
        return True


def load_from_string(synthfun_str):
    """
    Returns a SyGuSGrammar object representing the given string. The string is expected to be a valid synth-fun 
    command (refer SyGuS 2.0 format: https://sygus.org/language/).  
    :param synthfun_str: string  
    :return: SyGuSGrammar  
    """
    # Parse string into nested lists of atomic strings.
    nested_list = lisplike.parser(synthfun_str)
    # Construct SyGuSGrammar object from nested list representation.
    if len(nested_list) != 6:
        raise ValueError('Must have the form (synth-fun name arguments return-type predeclarations grouped-rule-list)')
    command, name, parameters, range_type, predeclarations, grouped_rule_list = nested_list
    if command != 'synth-fun':
        raise ValueError('Input does not contain a synth-fun command.')
    grammar = SyGuSGrammar()
    grammar.name_synth_fun(name)
    try:
        grammar.specify_parameters([tuple(param) for param in parameters])
    except Exception:
        raise ValueError('Parameter list must be of the form ((param_name1 param_type1) (param_name2 param_type2) ...)')
    grammar.define_range(range_type)
    try:
        grammar.add_nonterminals([tuple(predecl) for predecl in predeclarations])
    except Exception:
        raise ValueError('Predeclarations must be of the form ((nonterminal1 type1) (nonterminal2 type2) ...)')
    for group in grouped_rule_list:
        nonterminal, nonterminal_type, rule_list = group
        declared_type = next(predecl[1] for predecl in predeclarations if predecl[0] == nonterminal)
        if nonterminal_type != declared_type:
            raise ValueError('Nonterminal {} was declared to be of type {} but '
                             'rule list contains {}'.format(nonterminal,
                                                            lisplike.pretty_string(declared_type, noindent=True),
                                                            lisplike.pretty_string(nonterminal_type, noindent=True)))
        for rule in rule_list:
            grammar.add_rule(nonterminal, rule)
    return grammar


# Helper function for SMTGrammar class
# Implemented here in order to not expose the internals of the class
def track_nonterminals_one_step(sygus_grammar):
    """
    Dictionary of nonterminals produced post the expansion of a rule from a given nonterminal.  
    The keys are nonterminals and the values are a list of lists of nonterminals. The order of the outer 
    list is the same as the order of the rules given by get_ordered_rule_list. The order of nonterminals in the 
    inner list is arbitrary but deterministic.  
    :param sygus_grammar: SyGuSGrammar  
    :return: dict {string: list of list of string}  
    """
    ordered_rule_dict = sygus_grammar.get_ordered_rule_list()
    post = dict()
    nonterminals = {typed_nonterminal[0] for typed_nonterminal in sygus_grammar.get_typed_nonterminal_set()}
    for nonterminal in nonterminals:
        # For each nonterminal, for each of its production rules in the order in which they appear in the rule
        # list, store the nonterminals produced by the rule expansion.
        ordered_post_list = []
        for rule in ordered_rule_dict[nonterminal]:
            # Sort the list before adding it in order to make the computation deterministic.
            ordered_post_list.append(
                sorted([nonterminal for nonterminal in nonterminals if lisplike.is_subexpr_repr(nonterminal, rule)]))
        post[nonterminal] = ordered_post_list
    return post
