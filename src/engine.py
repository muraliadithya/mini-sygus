"""
Script to call from terminal and run miniature SyGuS engine.
Argument after script call should be the name of the input file containing
SyGuS grammar descriptions. The engine will write a file with the SyGuS grammars
replaced by constraint grammars (with the synthesized lemmas). A solver (currently
only CVC4) is then called on the written file to determine satisfiability.
If sat, then the solver's model is obtained and applied to each synthesized lemma,
then printed to the terminal.
"""

import sys
from src.engine_utils import *

args = sys.argv[1:]
if args:
    infile_name = args[0]
    smtfile_name = get_outfile_name(infile_name)
    grammars = sygus_to_constraint(infile_name, smtfile_name)
    model = call_solver(smtfile_name, grammars)