"""
Script to call from terminal and run minimal SyGuS engine.  
"""

import argparse

from solver.engine import solve


parser = argparse.ArgumentParser(description='A minimal SyGuS solver based on constraint solving.')
parser.add_argument('infile', help='Input file')
parser.add_argument('--smtsolver', choices=['z3', 'cvc4'], default='z3', 
                    help='Choice of backend SMT solver.')
# parser.add_argument('--timeout', type=int, default=None, 
#                     help='Total timeout in seconds. No timeout given by default.')
parser.add_argument('--num-solutions', '-N', metavar='num_solutions', type=int, default=1, 
                    help='Find multiple solutions to the SyGuS problem.')

args = parser.parse_args()
solve(args)
