# mini-sygus
A minimal constraint-based syntax-guided synthesis (SyGuS) engine  
The current version of the solver has a very restricted use-case of 
SyGuS problems where the grammars are finite and the 
constraints have only ground terms, i.e., quantifier-free.  


## Requirements

- [Python 3.5 or above](https://www.python.org/downloads/)
- An SMT solver. Currently the following solvers are supported:
  - [Z3 4.8.9](https://github.com/Z3Prover/z3/releases/tag/z3-4.8.9) (default choice)
  - [CVC4 1.9](https://cvc4.github.io/downloads.html)

## Installation
- Clone the master branch
- Install the requirements. Running `z3 -h` or `cvc4 -h` 
  should work depending on the solver of your choice.
- Add the repo top level `mini-sygus` to `PYTHONPATH` and 
  `mini-sygus/scripts` directory to `PATH`.
- The synthesis engine should be installed. You should 
  be able to run `minisy -h` from the terminal.


## Usage examples
The entry script into the solver is `scripts/minisy`. 
It comes with a help message:
```
python3 scripts/minisy -h
```

```
usage: minisy [-h] [--smtsolver {z3,cvc4}] [--num-solutions num_solutions]
                 infile

A minimal SyGuS solver based on constraint solving.

positional arguments:
  infile                Input file

optional arguments:
  -h, --help            show this help message and exit
  --smtsolver {z3,cvc4}
                        Choice of backend SMT solver.
  --num-solutions num_solutions, -N num_solutions
                        Find multiple solutions to the SyGuS problem.

```

In order to call the solver from anywhere, the `scripts` 
directory is added to `PATH` and the repo toplevel 
should be added to `PYTHONPATH`.
On Linux this can be done by adding the 
following lines to `.bashrc` (`.zshrc` on Mac) :
```
export PYTHONPATH="/path/to/repo/mini-sygus/":$PYTHONPATH
export PATH="/path/to/repo/mini-sygus/scripts/":$PATH
```

The solver can be run with either Z3 or CVC4. 
Here is the same synthesis problem solved using both:
```
python3 scripts/minisy tests/min2.sy 
sat
(define-fun minint ((x Int) (y Int)) Int
(ite (<= x y) x y)
)
```

```
python3 scripts/minisy tests/min2.sy --smtsolver=cvc4 
sat
(define-fun minint ((x Int) (y Int)) Int
(ite (<= y x) y x)
)

```

The solver creates a `.tmp` subdirectory in the same 
directory as the input to generate temporary/intermediate files. This
is not removed automatically.

It is possible to ask for multiple solutions at a time, although 
this capability is restricted:
```
python3 scripts/minisy tests/add2.sy --num-solutions=2
sat
(define-fun add2 ((x Int) (y Int)) Int
(doplus x y)
)

sat
(define-fun add2 ((x Int) (y Int)) Int
(doplus y x)
)
```

The solver returns `unsat` when it runs out of solutions:
```
python3 scripts/minisy tests/add2.sy --num-solutions=3
sat
(define-fun add2 ((x Int) (y Int)) Int
(doplus x y)
)

sat
(define-fun add2 ((x Int) (y Int)) Int
(doplus y x)
)
```

Input files must be written in SyGuS 2.0 format 
(see https://sygus.org/language/). Currently this is only enforced 
loosely. The `synth-fun` command itself must be according to 
the format, but otherwise it is expected that the theory-specific 
operators used in the problem are those that can be accepted by the 
corresponding backend solver used.  
Here is an example where the operators are specific to Z3:
```
python3 scripts/minisy tests/trivial_example_z3.sy 
sat
(define-fun insert ((x Int) (y (Array Int Bool))) (Array Int Bool)
(store y x true)
)
```

## Info

Feature summary:
- Update solver to use either Z3 or CVC4 as the backend
- Make solver print a help message with usage text and options
- Multiple solutions

To do:
- Checking for the validity of a given synthesis solution
- Symmetry reduction to eliminate redundant solutions when 
  multiple solutions are being proposed
- Counterexample generation for quantified constraints
