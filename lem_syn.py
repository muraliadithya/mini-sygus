import re, time
import subprocess, itertools, warnings
from utils import *

class grammar():
    def __init__(self, filename='', p=True, w=True, r=False,
                 grammar_count=1, line_delay=0, counts_init={},
                 outfile=None):
        self.filename = filename
        self.success = False
        self.line_start = 0
        self.line_end = 0
        self.lemma_name = ''
        self.arguments = {}
        self.symbols = {}
        self.replacements = []
        self.rules = {}
        self.counts_init = counts_init
        if 'bools' not in self.counts_init:
            self.counts_init['bools'] = 0
        self.counts = {}
        self.lemma = ''
        self.bools = 0
        self.functions = {}

        if self.filename:
            self.success = self.read_input(grammar_count, line_delay)
            if self.success:
                self.process_rules()
                self.compute()
                if p:
                    self.print_output()
                if w:
                    self.write_output(outfile)
                if r:
                    self.replace_output()
            elif p:
                print('Unsuccessful read; verify grammar count in file')
    
    def read_input(self, count, delay):
        with open(self.filename) as f:
            d = 0
            predec = False
            rules = False
            for c,line in enumerate(f):
                if (delay > 0 or line.isspace() or
                    (';' in line and line[:line.find(';')].isspace())):
                    delay -= 1
                    continue
                d += depth(line)
                if predec:
                    d_rules = d + 1
                    predec = False
                    self.symbols = parse_arguments(line)
                    rules = True
                    rule_curr = []
                elif rules:
                    rule_curr.extend([s for s in re.split(' |\n', line) if s])
                    if d <= d_rules and len(rule_curr) > 0:
                        if len(rule_curr[0]) > 1 and rule_curr[0][1] == '(':
                            rule_curr[0] = rule_curr[0][1:]
                        r = ' '.join(rule_curr)
                        if set(r) - {'(',')'}:
                            self.replacements.append(r)
                        rule_curr = []
                    if d < d_rules - 1:
                        self.line_end = c
                        rules = False
                        break
                elif '(synth-fun ' == line[:11]:
                    self.lemma_name = line.split(' ')[1]
                    count -= 1
                    if count == 0:
                        self.line_start = c
                        self.arguments = parse_arguments(line[1:])
                        predec = True
        return count == 0
    
    def compute(self):
        self.recount()
        self.compute_parameters('Start')
        self.compute_height('Start')
        self.compute_lemma()
        self.compute_functions()
        self.counts['bools'] = self.bools
        self.counts = {symbol: self.counts[symbol] for symbol in self.counts
                       if self.counts[symbol] != 0}
    
    def recount(self):
        self.counts = self.counts_init.copy()
        for symbol in self.symbols:
            if symbol not in self.counts:
                self.counts[symbol] = 0
        self.bools = self.counts_init['bools']
    
    def process_rules(self):
        symbols = set(self.symbols.keys())
        for rule in self.replacements:
            rule = rule.split(' ', 1)
            symbol = rule[0][1:]
            replacements = rule[-1].split('(',1)[-1][:-2]
            keys = get_keywords(replacements)
            self.rules[symbol] = {
                'replacements': parse_rules(replacements),
                'dependents': set(self.symbols.keys()).intersection(keys),
                'arguments': [var for var in self.arguments
                              if var in keys],
            }
    
    def compute_parameters(self, symbol):
        if not self.rules[symbol]['dependents']:
            self.rules[symbol]['parameters'] = set(self.rules[symbol]['arguments'])
        else:
            self.rules[symbol]['parameters'] = set().union(*[
                self.rules[s]['parameters'] if 'parameters' in self.rules[s] else self.compute_parameters(s)
                for s in self.rules[symbol]['dependents']
            ])
        return self.rules[symbol]['parameters']
    
    def compute_height(self, symbol):
        if not self.rules[symbol]['dependents']:
            self.rules[symbol]['height'] = 1
        else:
            self.rules[symbol]['height'] = 1 + max([
                self.rules[s]['height'] if 'height' in self.rules[s] else self.compute_height(s)
                for s in self.rules[symbol]['dependents']
            ])
        return self.rules[symbol]['height']
    
    def compute_lemma(self):
        self.lemma = self.translate(self.function_gen('Start'))
    
    def compute_functions(self):
        for symbol in sorted(self.symbols, key=lambda s: self.rules[s]['height'], reverse=True):
            self.functions[symbol] = []
            init = 0
            if symbol in self.counts_init:
                init = self.counts_init[symbol]
            for f in range(init, self.counts[symbol]):
                self.functions[symbol].append(
                    '(define-fun {}{} ({}) {}\n{}\n)'.format(
                        symbol,
                        f+1 if not symbol[-1].isdigit() else ''.join(['_',str(f+1)]),
                        ' '.join(['({} {})'.format(arg, self.arguments[arg])
                                  for arg in self.arguments
                                  if arg in self.rules[symbol]['parameters']]),
                        self.symbols[symbol],
                        self.translate(self.function_gen(symbol)),
                    )
                )
    
    def translate(self, statement):
        dependents = [symbol for symbol in self.symbols if symbol in statement]
        nonterminals = sorted(dependents, key=lambda s: self.rules[s]['height'], reverse=True)
        while nonterminals:
            symbol = nonterminals.pop(0)
            m = len(symbol)
            indices = find_unreplaced(statement, symbol) + [len(statement)]
            S = statement[:indices[0]]
            for i in range(len(indices)-1):
                S += self.expand_symbol(symbol) + statement[indices[i]+m:indices[i+1]]
            statement = S
            nonterminals.extend(self.rules[symbol]['dependents'])
            for sym in self.rules[symbol]['dependents']:
                for i in range(len(nonterminals)):
                    if self.rules[sym]['height'] >= self.rules[nonterminals[i]]['height']:
                        break
                nonterminals.insert(i, sym)
        return statement
    
    def function_gen(self, symbol):
        rules = self.rules[symbol]['replacements']
        n = len(rules)
        if n == 1:
            statement = rules[0]
        elif n > 1:
            # Could improve from n-1 to log_2 n many conditionals
            statement = ' '.join(['(ite b{} {}'.format(
                self.bools + j + 1,
                rule,
            ) for j,rule in enumerate(rules[:-1])])
            statement += ' {}{}'.format(rules[-1], ')'*(n-1))
            self.bools += n-1
        return statement
    
    def expand_symbol(self, symbol):
        rules = self.rules[symbol]['replacements']
        n = len(rules)
        if n == 1:
            replacement = rules[0]
        elif n > 1:
            self.counts[symbol] += 1
            replacement = ''.join([
                '(', symbol, '_' if symbol[-1].isdigit() else '',
                str(self.counts[symbol]), ' ',
                ' '.join([arg for arg in self.arguments
                          if arg in self.rules[symbol]['parameters']]),
                ')',
            ])
        return replacement
    
    def eliminate_bool(self, statement, model, symbol='Start'):
        i = statement.find('ite b') + 5
        j = i + 1
        while statement[j].isdigit():
            j += 1
        num = int(statement[i:j])
        k = 0
        while (k < len(self.rules[symbol]['replacements']) - 2 and
               not self.check_model(model, num+k)):
            k += 1
        delay = not self.check_model(model, num+k)
        j += 1
        choice = statement[j]
        d = depth(statement[j])
        while d > 0:
            j += 1
            choice += statement[j]
            d += depth(statement[j])
            if delay and d == 0:
                delay = False
                j += 2
                choice = statement[j]
                d += depth(statement[j])
        return choice
    
    def check_model(self, model, b):
        var = 'b' + str(b)
        return var in model and model[var]
    
    def apply_model(self, model, line='', symbol='Start', num=1):
        if line == '':
            statement = self.lemma
        else:
            index = num - 1
            if symbol in self.counts_init:
                index -= self.counts_init[symbol]
            statement = self.functions[symbol][index]
        while 'ite b' in statement:
            statement = self.eliminate_bool(statement, model, symbol)
        for symb, n in set().union(*[find_replaced(statement, symb) for symb in self.symbols]):
            statement = self.apply_model(model, statement, symb, n)
        if line == '':
            line = statement
        else:
            line = line.replace(self.func_name(symbol, num), statement)
        return line
    
    def func_name(self, symbol, num):
        func = ''.join([symbol, '_' if symbol[-1].isdigit() else '', str(num)])
        name =  ''.join(['(', func, ' ', ' '.join([arg for arg in self.arguments
                                                   if arg in self.rules[symbol]['parameters']]),
                         ')'])
        return name
    
    def del_rule(self, symbol, num):
        rule = ''
        if symbol in self.rules and num < len(self.rules[symbol]['replacements']):
            rule = self.rules[symbol]['replacements'].pop(num)
            self.compute()
            print('Deleted rule: {} to {}'.format(symbol, rule))
        else:
            print('Invalid symbol/rule.')
        return rule
    
    def enf_rule(self, symbol, num):
        rule = ''
        if symbol in self.rules and num < len(self.rules[symbol]['replacements']):
            rule = self.rules[symbol]['replacements'][num]
            self.rules[symbol]['replacements'] = [rule]
            self.compute()
            print('Enforced rule: {} to {}'.format(symbol, rule))
            print('Deleted all other rules for symbol {}'.format(symbol))
        else:
            print('Invalid symbol/rule.')
        return rule
    
    def add_rule(self, symbol, rule):
        if symbol in self.rules and depth(rule) == 0:
            self.rules[symbol]['replacements'].append(rule)
            self.compute()
            print('Added rule: {} to {}'.format(symbol, rule))
        else:
            print('Invalid symbol/rule.')
        return rule
    
    def print_bools(self):
        for b in range(self.counts_init['bools'], self.bools):
            print('(declare-const b{} Bool)'.format(b+1))
    
    def print_functions(self):
        for symbol in sorted(self.symbols, key=lambda s: self.rules[s]['height']):
            for func in self.functions[symbol]:
                print(func)
    
    def print_lemma(self):
        print('(define-fun {} ({}) Bool\n{})'.format(
            self.lemma_name,
            ' '.join(['({} {})'.format(arg, self.arguments[arg])
                      for arg in self.arguments]),
            indent(self.lemma),
        ))
    
    def print_output(self):
        self.print_bools()
        print('')
        self.print_functions()
        print('')
        self.print_lemma()
        
    def return_output(self):
        out = ['(declare-const b{} Bool)'.format(b+1)
               for b in range(self.counts_init['bools'], self.bools)]
        out.extend([' '.join(func.split('\n'))
                    for symbol in sorted(self.symbols, key=lambda s: self.rules[s]['height'])
                    for func in self.functions[symbol]])
        out.append('(define-fun {} ({}) Bool {})'.format(
            self.lemma_name,
            ' '.join(['({} {})'.format(arg, self.arguments[arg])
                      for arg in self.arguments]),
            ' '.join(self.lemma.split('\n')),
        ))
        return out
    
    def write_output(self, outfile, mode='w'):
        if not outfile:
            index = self.filename.rfind('/')
            outfile = self.filename[:index] + '/output' + self.filename[index:-4] + '_syn.txt'
        with open(outfile, mode) as file:
            for b in range(self.counts_init['bools'], self.bools):
                file.write('(declare-const b{} Bool)\n'.format(b+1))
            file.write('\n')
            for symbol in sorted(self.symbols, key=lambda s: self.rules[s]['height']):
                for func in self.functions[symbol]:
                    file.write(func)
                    file.write('\n')
            file.write('\n')
            file.write('(define-fun {} ({}) Bool\n{})'.format(
                self.lemma_name,
                ' '.join(['({} {})'.format(arg, self.arguments[arg])
                          for arg in self.arguments]),
                indent(self.lemma),
            ))
    
    def replace_output(self, repfile=None, mode='w'):
        if not repfile:
            index = self.filename.rfind('/')
            repfile = self.filename[:index] + '/output' + self.filename[index:-4] + '_repl.txt'
        with open(repfile, mode) as file:
            with open(self.filename) as infile:
                for c,line in enumerate(infile):
                    if c < self.line_start:
                        file.write(line)
                    elif c == self.line_start:
                        for b in range(self.counts_init['bools'], self.bools):
                            file.write('(declare-const b{} Bool)\n'.format(b+1))
                        file.write('\n')
                        for symbol in sorted(self.symbols, key=lambda s: self.rules[s]['height']):
                            for func in self.functions[symbol]:
                                file.write(func)
                                file.write('\n')
                        file.write('\n')
                        file.write('(define-fun {} ({}) Bool\n{})'.format(
                            self.lemma_name,
                            ' '.join(['({} {})'.format(arg, self.arguments[arg])
                                      for arg in self.arguments]),
                            indent(self.lemma),
                        ))
                        file.write('\n')
                    elif c <= self.line_end:
                        continue
                    else:
                        file.write(line)
    


def read_grammars(filename):
    grammars = []
    i = 0
    counts_init = {}
    while i == 0 or G.success:
        i += 1
        G = grammar(filename, grammar_count=i, counts_init=counts_init,
                    p=False, w=False)
        counts_init = G.counts
        if G.success:
            grammars.append(G)
    return grammars

def replace_grammars(filename, repfile=None, mode='w'):
    grammars = read_grammars(filename)
    if len(grammars) == 0:
        return
    if not repfile:
        index = filename.rfind('/')
        repfile = filename[:index] + '/output' + filename[index:-4] + '_repl.txt'
    with open(repfile, mode) as file:
        with open(filename) as infile:
            i = 0
            G = grammars[i]
            for c,line in enumerate(infile):
                if c < G.line_start:
                    file.write(line)
                elif c == G.line_start:
                    for b in range(G.counts_init['bools'], G.bools):
                        file.write('(declare-const b{} Bool)\n'.format(b+1))
                    file.write('\n')
                    for symbol in sorted(G.symbols, key=lambda s: G.rules[s]['height']):
                        for func in G.functions[symbol]:
                            file.write(func)
                            file.write('\n')
                    file.write('\n')
                    file.write('(define-fun {} ({}) Bool\n{})'.format(
                        G.lemma_name,
                        ' '.join(['({} {})'.format(arg, G.arguments[arg])
                                  for arg in G.arguments]),
                        indent(G.lemma),
                    ))
                    file.write('\n')
                elif c <= G.line_end:
                    continue
                else:
                    i += 1
                    if i < len(grammars):
                        G = grammars[i]
                    file.write(line)
    return grammars, repfile

def operate(filename, p=True):
    grammars, smt_file = replace_grammars(filename)
    start = time.time()
    proc = subprocess.Popen('cvc4 {} -m --lang=smt2'.format(smt_file), shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    cvc4_out, err = proc.communicate()
    if p:
        print('runtime: {:.2f}s'.format(time.time()-start))
        print(cvc4_out)
    if cvc4_out == '':
        if p:
            print(err)
    else:
        cvc4_lines = cvc4_out.split('\n')
        if cvc4_lines[0] == 'sat':
            model = {}
            for line in cvc4_lines:
                if 'define-fun' in line:
                    line = line.split(' ')
                    model[line[1]] = line[4][:-1] == 'true'
            if p:
                print('sat')
                for G in grammars:
                    print('\nsynth {}:\n{}'.format(G.lemma_name, G.lemma))
                    print('model {}:\n{}'.format(G.lemma_name, G.apply_model(model)))
        elif p:
            print('unsat')
    