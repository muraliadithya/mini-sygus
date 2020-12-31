from src.SyGuSGrammar import load_from_string

synthfun_str = """
(synth-fun lemma ((x Int) (y (Set Int))  ) Bool
           ((Start Bool) (B1 Bool) (B2 Bool) (B3 Bool) (Loc Int))

           ((Start Bool (
                  (=> B1 (and B2 B3))))
           (B1 Bool
                  ((member Loc (hbst Loc))))
          (B2 Bool
                  ((<= (key Loc) (maxr Loc))))
           (B3 Bool
                  ((<= (minr Loc) (key Loc))))
           (Loc Int (x
                     y))

))
"""

grammar = load_from_string(synthfun_str)
for key in grammar.__dict__:
    print('{}: {}'.format(key, getattr(grammar, key)))

for key in grammar.nonterminals:
    print('{}:'.format(key))
    for rule in grammar.rules[key]:
        print(rule)