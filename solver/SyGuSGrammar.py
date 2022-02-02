import functools
import re

import solver.lisplike as lisplike


# NOTE: Some argument/output types are written as lisplike.is_lisplike. This is currently enforced nowhere.
# Need to provide tighter integration with lisplike data types and checking in a way that can be clearly inferred.
# This is complicated by the fact that the nested list data structure is deconstructed very often, which makes a 
# solution to encapsulate in order to provide abstraction difficult to use, and possibly pointless.

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
        self.typed_nonterminals = dict()
        self.start_symbol = None
        self.rules = dict()

        # Attributes for caching useful values/values that are expensive to compute
        # IMPORTANT: No support for checking whether cached values are correct. Use with caution.
        # Dictionary of nonterminals produced post the expansion of a rule from a given nonterminal
        self.post = None
        # Set of admissible strings in the grammar
        self.admiss = None
        # Minimum and maximum depths required/possible to unpack grammar to some admissible string
        self.min_depth = None
        self.max_depth = None

    def name_synth_fun(self, name):
        """
        Name of the function to be synthesised.  
        :param name: string  
        """
        self.name = name

    def specify_parameters(self, typed_params_list):
        """
        Ordered list of input parameter names and types for the synthesised function.  
        :param typed_params_list: list of (string, lisplike.is_lisplike)  
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
        :param smt_type: lisplike.is_lisplike  
        """
        self.range_type = smt_type

    def add_nonterminal(self, nonterminal, smt_type):
        """
        Nonterminal in the grammar.  
        :param nonterminal: string  
        :param smt_type: lisplike.is_lisplike  
        """
        if nonterminal in self.typed_nonterminals and smt_type != self.typed_nonterminals[nonterminal]:
            raise ValueError('Nonterminal {} already declared '
                             'with type {}.'.format(nonterminal, self.typed_nonterminals[nonterminal]))
        self.typed_nonterminals[nonterminal] = smt_type

    def add_nonterminals(self, typed_nonterminals_list):
        """
        Nonterminals in the grammar. The first nonterminal in the list is assumed to be the start symbol if one 
        is not defined already.  
        :param typed_nonterminals_list: list of (string, lisplike.is_lisplike)  
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
        if start_symbol_name not in self.typed_nonterminals:
            raise ValueError('{} is not a valid nonterminal'.format(start_symbol_name))
        current_start_symbol = self.start_symbol
        if current_start_symbol is not None and start_symbol_name != current_start_symbol:
            raise ValueError('{} already declared as the start symbol.'.format(current_start_symbol))
        self.start_symbol = start_symbol_name

    def add_rule(self, nonterminal, rule):
        """
        Add a production rule for a nonterminal.  
        :param nonterminal: string  
        :param rule: lisplike.is_lisplike  
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
        :return: list of (string, lisplike.is_lisplike)  
        """
        return list(self.parameters.items())

    def get_range_type(self):
        """
        Return the range of the function to be synthesised as an smt type in lisp-like representation.  
        :return: lisplike.is_lisplike  
        """
        return self.range_type

    def get_typed_nonterminal_list(self):
        """
        Return the set of nonterminals in the grammar with their types.  
        :return: list of (string, lisplike.is_lisplike)  
        """
        return list(self.typed_nonterminals.items())

    def get_nonterminal_set(self):
        """
        Return the set of nonterminals in the grammar.  
        :return: set of string  
        """
        # TODO (low): cache this value in a class attribute in a way that can be updated when the value becomes stale.
        return {nonterminal for nonterminal in self.typed_nonterminals}

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
        :return: dict {string: list of lisplike.is_lisplike}  
        """
        nonterminals = list(nonterminals)
        if not nonterminals:
            # No nonterminals specified
            nonterminals = self.get_nonterminal_set()
        return {nonterminal: sorted(self.rules[nonterminal], key=functools.cmp_to_key(lisplike.less_than)) 
                for nonterminal in nonterminals}

    def get_one_step_dict(self):
        """
        Compute the set of nonterminals that occur in each production rule for each nonterminal.
        :return: dict {string: list [string]}
        """
        # See if the relevant caching attribute holds a valid value
        if self.post is None:
            self.post = track_nonterminals_one_step(self)
        one_step_dict = dict()
        nonterminals = self.get_nonterminal_set()
        for nt in nonterminals:
            one_step_set = {symbol for symbols_per_rule in self.post[nt] for symbol in symbols_per_rule} 
            one_step_dict[nt] = one_step_set
        return one_step_dict

    def is_finite(self):
        """
        Check whether the grammar only has finite productions.  
        A grammar has an infinite production if there is a sequence of nonterminals B_1, B_2, ... B_n 
        such that B_i has a rule that contains B_i+1 in its expansion, and B_n contains B_1.  
        :return: bool  
        """
        one_step_dict = self.get_one_step_dict()

        # Auxiliary function to recurse on each nonterminal and check for repeated occurrence
        def is_finite_check_and_recurse(nonterminal=self.get_start_symbol(), seen_nonterminals=set()):
            if nonterminal in seen_nonterminals:
                # Repeated occurrence. Grammar is not finite.
                return False
            else:
                # The nonterminal is now a seen symbol.
                seen_nonterminals.add(nonterminal)
                # Recurse on all nonterminals reachable from the current one in one step
                return all(is_finite_check_and_recurse(symbol, seen_nonterminals) 
                           for symbol in one_step_dict[nonterminal])

        # Call auxiliary function to check for finiteness and return the value
        return is_finite_check_and_recurse()

    def is_terminable(self):
        """
        Check whether the grammar is either finite or has infinite-but-permissible replacement rules.
        Here, permissible refers to each symbol having a replacement rule path to eliminating all nonterminals.
        :return bool:
        """
        if self.is_finite():
            return True

        # Auxiliary function to obtain set of terminating symbols which dependent on the input nonterminal.
        def terminable_aux(nonterminal=self.get_start_symbol(),
                           seen_nonterminals=set(), terminating_symbols=set()):
            if nonterminal in seen_nonterminals:
                # Repeated occurrence. This particular path is not a termination.
                return terminating_symbols
            else:
                # The nonterminal is now a seen symbol.
                seen_nonterminals.add(nonterminal)
                for rule_symbols in self.post[nonterminal]:
                    rule_terminates = True
                    for symbol in rule_symbols:
                        if symbol not in terminating_symbols:
                            terminating_symbols = terminable_aux(symbol, seen_nonterminals, terminating_symbols)
                        if symbol not in terminating_symbols:
                            # If some symbol in rule is interminable, then the rule is considered so
                            rule_terminates = False
                    if rule_terminates:
                        # If some rule is terminable, then the symbol is considered so
                        nonterminal_terminates = True
                        terminating_symbols.add(nonterminal)
                return terminating_symbols

        # Call auxiliary function to check for terminability of all symbols
        return len(terminable_aux()) == len(self.post)

    def get_nonterminal_heights(self, least=True):
        """
        Return a dictionary of nonterminals in the grammar with value representing each nonterminal
        symbol's either least or most height. The least height is the least number of successive replacement
        rule applications necessary to eliminate nonterminals, which is always finite for a well-defined
        grammar. The most height is the most such number, and is only necessarily finite for finite grammars
        (i.e. grammars without self-referential rules).
        :param least: bool
        :return: dict {string: int}
        """
        if not self.is_finite():
            if not least:
                raise ValueError('Grammar is not finite. Nonterminal most heights are possibly infinite.')
            elif not self.is_terminable():
                raise ValueError('Grammar contains rule sets which are exclusively self-referential.\n' +
                                 'Nonterminal least heights are possibly infinite.')
        one_step_dict = self.get_one_step_dict()
        empty_nonterminals = [nt for nt, rules in self.rules.items() if len(rules) == 0]
        if len(empty_nonterminals) != 0:
            raise ValueError(f'Nonterminals {", ".join(empty_nonterminals)} have no productions. Unsupported.')

        # Auxiliary function to determine nonterminal bottom-up heights from terminals.
        # The least height of a nonterminal is the length of the shortest path of replacement
        # rules to an admissible string, which is always finite. The most height is the longest such path,
        # which may be infinite if the grammar is infinite.
        func_rule = min if least else max

        def aux_heights(nonterminal=self.get_start_symbol(), nt_heights=dict(), seen_symbols=set()):
            seen_symbols.add(nonterminal)
            # Initialize height to None
            nt_heights[nonterminal] = None
            # Compute heights of all nonterminals that the current one depends on first.
            if one_step_dict[nonterminal]:
                for symbol in one_step_dict[nonterminal]:
                    if symbol not in seen_symbols:
                        nt_heights.update(aux_heights(symbol, nt_heights, seen_symbols))
            # The height of a rule (independent of least or most option) is the maximum of the heights of all the
            # nonterminals appearing in it. A rule without any nonterminals is of height 0.
            # Rules with symbols higher in the topological order (whose heights may not be computed yet and show up as
            # None) cause infinite grammars and can therefore be ignored since:
            # (1) infinite grammars should not reach this point for greatest height computation, and
            # (2) infinite paths do not contribute to least height computation.
            rule_heights = [0 if len(nt_symbols) == 0 else max(nt_heights[symbol] for symbol in nt_symbols)
                            for nt_symbols in self.post[nonterminal]
                            if all(nt_heights.get(nt, None) is not None for nt in nt_symbols)]
            # Height of a nonterminal is one more than the rules it has, since it adds a derivation step.
            try:
                nt_heights[nonterminal] = 1 + func_rule(rule_heights)
            except ValueError:
                # Code should not reach this point. Unless the grammar is infinite (for most) or
                # not terminable (for least), rule_heights should be a nonempty list.
                raise Exception(f'Unable to calculate {"least" if least else "greatest"} height of productions from '
                                f'nonterminal {nonterminal}. Something has gone wrong.')
            return nt_heights
        return aux_heights()

    def get_minimum_depth(self):
        """
        Return the minimum required depth to obtain an admissible string.
        :return: int
        """
        if self.min_depth is None:
            self.min_depth = self.get_nonterminal_heights(least=True)[self.start_symbol]
        return self.min_depth

    def get_maximum_depth(self):
        """
        Return the maximum possible depth to obtain an admissible string from a finite grammar.
        :return: int
        """
        if self.max_depth is None and self.is_finite():
            self.max_depth = self.get_nonterminal_heights(least=False)[self.start_symbol]
        return self.max_depth

    def get_ordered_nonterminal_list(self):
        """
        Return a list of nonterminals in the grammar, ordered by dependence by expansion containment
        such that the nonterminals whose expansions contain no nonterminals are first and the start
        symbol is last.
        This function requires a finite grammar (without self-referential rules).
        :return: list of string  
        """
        nonterminal_heights = self.get_nonterminal_heights(least=False)
        # Obtain list of nonterminals sorted by increasing most height
        return sorted(nonterminal_heights, key=nonterminal_heights.get)

    def get_admissible_strings(self):
        """
        Return a set of admissible strings in the grammar.
        This assumes the grammar is finite and will do nothing if grammar is infinite.
        :return: set of string  
        """
        # See if the relevant caching attribute holds a valid value
        if self.admiss is None and self.is_finite():
            # Ordered list of nonterminals
            nt_list = self.get_ordered_nonterminal_list()[::-1]
            rules = self.get_ordered_rule_list()
            # Dictionary with values as sets of nonterminal strings.
            # Each key is the nonterminal which is earliest in nt_list.
            workdict = {symbol: set() for symbol in nt_list}
            workdict['Start'].add('Start')
            admissible_strings = set()
            for i, nonterminal in enumerate(nt_list):
                # Iterate through nonterminals (in order), pushing toward admissibility
                while workdict[nonterminal]:
                    string = workdict[nonterminal].pop()
                    for rule in rules[nonterminal]:
                        # Apply rule once to string
                        repl = string.replace(nonterminal, lisplike.pretty_string(rule, noindent=True), 1)
                        repl_split = re.split(' |\(|\)', repl)
                        # Identify the earliest (in order) nonterminal appearing in post-rule string
                        next_nonterminal = None
                        for symbol in nt_list[i:]:
                            if symbol in repl_split:
                                next_nonterminal = symbol
                                break
                        if next_nonterminal is None:
                            # String does not contain nonterminals, so is admissible
                            admissible_strings.add(repl)
                        else:
                            # Place post-rule string in workdict
                            workdict[next_nonterminal].add(repl)
            self.admiss = admissible_strings
        return self.admiss

    def is_admissible(self, lisp, symbol=None, rule=None):
        """
        Determine if a parsed lisp-like string is admissible in the SyGuS grammar.  
        The optional parameters specify an enforced starting symbol or replacement rule.
        This function is independent from get_admissible_strings and is more efficient.
        :param lisp: lisp-like string (list or string)  
        :param symbol: string  
        :param rule: lisp-like string (list or string)  
        """
        if lisp == []:
            return None
        if rule is None:
            # If no replacement rule is enforced, then enforce starting symbol.
            if symbol is None:
                symbol = self.start_symbol
            for i, nested_rule in enumerate(self.rules[symbol]):
                model = self.is_admissible(lisp, rule=nested_rule)
                if model is not None:
                    # If rule admits lisp, then return a certifying model.
                    if model == []:
                        return i
                    else:
                        return [i, model]
            # If no rule admisses lisp, then return None.
            return None

        # Auxiliary function to manage direct comparison of lisp content.
        def is_admissible_aux(lisp, rule):
            if isinstance(rule, str):
                if rule in self.typed_nonterminals:
                    # Rule is a nonterminal symbol.
                    return self.is_admissible(lisp, symbol=rule)
                else:
                    # Rule is a terminal symbol.
                    if isinstance(lisp, str) and lisp == rule:
                        return 'terminal'
                    else:
                        return None
            else:
                # Rule is a nested list; recurse.
                return self.is_admissible(lisp, rule=rule)

        # Cast lisplike structures to list if a single string.
        if isinstance(lisp, str):
            lisp = [lisp]
        if isinstance(rule, str):
            rule = [rule]
        # Iterate through strings/lists in lisp list, comparing each to the
        # corresponding element of the given replacement rule.
        models = []
        for j in range(len(lisp)):
            model = is_admissible_aux(lisp[j], rule[j])
            if model is None:
                # If any nested string/list is inadmissible by the corresponding
                # replacement rule, then lisp is inadmissible.
                return None
            elif model == 'terminal':
                # If terminal, then do not contribute toward model
                pass
            else:
                # If nonterminal, contribute certification to model
                models.append(model)
        # If all elements of lisp are admissible, then lisp is admissible.
        return models


def load_from_string(synthfun_str):
    """
    Returns a SyGuSGrammar object representing the given string. The string is expected to be a valid synth-fun 
    command (refer SyGuS 2.0 format: https://sygus.org/language/).  
    :param synthfun_str: string  
    :return: SyGuSGrammar  
    """
    # Parse string into nested lists of atomic strings.
    nested_list = lisplike.parse(synthfun_str)
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


# Helper function for ConstraintGrammar class
# Implemented here in order to not expose the internals of the class
def track_nonterminals_one_step(sygus_grammar):
    """
    Dictionary of nonterminals produced post the expansion of each rule of each nonterminal.  
    The keys are nonterminals and the values are a list of lists of nonterminals. The order of the outer 
    list is the same as the order of the rules given by get_ordered_rule_list (deterministic). The order of 
    nonterminals in the inner list is arbitrary but deterministic, and they appear with the same multiplicity with 
    which they appear in the corresponding expansion.  
    :param sygus_grammar: SyGuSGrammar  
    :return: dict {string: list of list of string}  
    """
    cached_post = sygus_grammar.post
    if cached_post is not None:
        return cached_post
    ordered_rule_dict = sygus_grammar.get_ordered_rule_list()
    post = dict()
    nonterminals = sygus_grammar.get_nonterminal_set()
    for nonterminal in nonterminals:
        # For each nonterminal, for each of its production rules in the order in which they appear in the rule
        # list, store the nonterminals produced by the rule expansion.
        ordered_post_list = []
        for rule in ordered_rule_dict[nonterminal]:
            # Check for the number of times each nonterminal appears in this rule and add it with that multiplicity
            nonterminals_in_rule = []
            for nt in nonterminals:
                nonterminals_in_rule = nonterminals_in_rule + [nt] * lisplike.count_subexpr(nt, rule)
            ordered_post_list.append(nonterminals_in_rule)
        # Sort the inner lists in order to make the computation deterministic.
        ordered_sorted_post_list = [sorted(occurring_nonterminals) for occurring_nonterminals in ordered_post_list]
        post[nonterminal] = ordered_sorted_post_list
    # Cache the post for next time
    sygus_grammar.post = post
    return post
