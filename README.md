# lemma-synthesis
a constraint-based syntax-guided synthesis (SyGuS) engine

## requirements

- [Python 3.5 or above](https://www.python.org/downloads/)
- [CVC4 1.9](https://cvc4.github.io/downloads.html)

## example
The following command runs the full solver using the input file `data/out_sdlist-dlist-and-slist.sy`. The engine detects all declared SyGuS grammars from the input file, synthesizes the corresponding lemmas and replaces the grammar descriptions with the lemmas in an output SMT file, runs the CVC4 solver on the output file, obtains a model (if satisfiable), and prints the synthesized lemmas instantiated according to the model.
```
python3 -m src.engine data/out_sdlist-dlist-and-slist.sy
```

```
sat

(define-fun lemma ((x Int) (nil Int)) Bool
(not (sdlst (prv nil)))
)

(define-fun rswitch () Int
0
)
```

## info

See `test_driver.ipynb` for examples on useful features of `lem_syn` module. See `tests/` for examples of input grammar files and their corresponding output lemmas. The first example of `test_driver.ipynb` reveals to current extend of this program: multiple grammars are read from an input text file, replaced by respective (and disjoint) synthesized lemmas, ported to CVC4 in order to verify satisfiability and generate a satisfying model, then applies the reported model to the synthesized lemmas to instantiate the particular lemmas which satisfy the other constraints in the given file.

Generally, `lem_syn` creates a `grammar` object sourced from the input file description of a finite, context-free grammar in SyGuS format. This `grammar` object is then able to compute a set of boolean flow variables, auxiliary functions, and a synthesized lemma detailing the expanded form of the grammar. This lemma (with variables and functions) can then replace the originating grammar; the resulting file (in SMT-Lib format) can then be ported to an SMT solver (CVC4).

By appending `(check-sat)` and `(get-model)`, a model satisfying the synthesized lemma will be obtained. Then, in dictionary form with boolean variable names as keys and the model assignments as the values, the model may be applied to the originating `grammar` lemma to simplify the synthesized lemma into the form instatiated by the model.

Feature summary:
- print/write boolean variables, auxiliary functions, and synthesized lemma in SMT-Lib format
- replace grammar description by synthesized lines in copy of input file
- edit grammar after initial read (deleting, enforce, and add replacement rules for existing symbols)
- maintain multiple grammars within a single input file
- call CVC4 on synthesized lemma and given constraints to check satisfiability and, if satisfiable, generate a model
- apply model to synthesized lemma and collapse down output into a single 'instantiated lemma' statement without boolean variables or auxiliary functions
