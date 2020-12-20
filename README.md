# lemma-synthesis
a constraint-based syntax-guided synthesis (SyGuS) engine

See `test_driver.ipynb` for examples on useful features of `lem_syn` module.

Generally, `lem_syn` creates a `grammar` object sourced from the input file description of a finite, context-free grammar in SyGuS format. This `grammar` object is then able to compute a set of boolean flow variables, auxiliary functions, and a synthesized lemma detailing the expanded form of the grammar. This lemma (with variables and functions) can then replace the originating grammar; the resulting file (in SMT-Lib format) should then be ported to an SMT solver like CVC4 or Z3.

By appending `(check-sat)` and `(get-model)`, a model satisfying the synthesized lemma should be obtained. Then, in dictionary form with boolean variable names as keys and the model assignments as the values, the model may be applied to the originating `grammar` lemma to simplify the synthesized lemma into the form instatiated by the model.

Feature summary:
- print/write boolean variables, auxiliary functions, and synthesized lemma in SMT-Lib format
- replace grammar description by synthesized lines in copy of input file
- edit grammar after initial read (deleting, enforce, and add replacement rules for existing symbols)
- apply model (given as dictionary) to synthesized lemma and collapse down output into a single 'instantiated lemma' statement without boolean variables or auxiliary functions
- read/maintain multiple grammars within a single input file

Features-in-development:
- correct calls of file (after grammar is replaced by synthesized lemma) to CVC4 (or Z3) for checking satisfiability and obtaining a model (if `sat`); currently, this satisfying model is provided by the user
