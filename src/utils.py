import re

def find_unreplaced(line, symbol):
    m = len(symbol)
    return [w.start() for w in re.finditer(symbol, line)
            if not line[w.start()+m].isdigit() and line[w.start()+m] != '_']

def find_replaced(line, symbol):
    m = len(symbol)
    repl = []
    for w in [w.start() for w in re.finditer(symbol, line)
              if line[w.start()+m].isdigit() or line[w.start()+m] == '_']:
        num = ''
        s = w + m
        while s < len(line) and (line[s].isdigit() or line[s] == '_'):
            num += line[s]
            s += 1
        if num[0] == '_':
            num = num[1:]
        repl.append((symbol, int(num)))
    return repl

def parse_arguments(line):
    line = line[line.find('(', 2)+1:]
    i = 0
    d = 0
    args = []
    arg_curr = ''
    while d >= 0 and i < len(line):
        c = line[i]
        d += depth(c)
        arg_curr += c
        if d == 0:
            if not arg_curr.isspace():
                args.append(arg_curr[1:-1])
            arg_curr = ''
        i += 1
    args_dict = {}
    for arg in args:
        s = arg.split(' ', 1)
        args_dict[s[0]] = s[1]
    return args_dict

def parse_rules(replacement):
    rules = []
    rule_curr = ''
    d = 0
    for w in replacement.split(' '):
        d += depth(w)
        rule_curr += w + ' '
        if d <= 0:
            if not rule_curr.isspace():
                while len(rule_curr) > 0 and (depth(rule_curr) < 0 or rule_curr[-1].isspace()):
                    rule_curr = rule_curr[:-1]
                rules.append(rule_curr)
            rule_curr = ''
    return rules

def get_keywords(words):
    return set([w for w in re.split('\(|\)|\n| ', ''.join(words)) if w not in {'', ' '}])

def depth(line):
    return line.count('(') - line.count(')')

def indent(output):
    output = output.split(' ')
    d = 0
    d_ref = [0]
    ind_ref = [0]
    ind_curr = 0
    for i,word in enumerate(output):
        d += depth(word)
        ind_curr += len(word) + 1
        if d <= d_ref[-1]:
            if d < d_ref[-1]:
                while d < d_ref[-1]:
                    d_ref.pop(-1)
                    ind_ref.pop(-1)
            output[i] += '\n' + ' '*(ind_ref[-1]-1)
            ind_curr = 0
        if word in {'(=>', '(ite', '(and', '(or', '(<='}:
            d_ref.append(d)
            ind_ref.append(ind_ref[-1]+ind_curr)
            ind_curr = 0
    return ' '.join(output)