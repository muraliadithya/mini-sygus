"""
Main engine of the minimal SyGuS solver.  
"""

import os
from solver.engine_utils import *

MAX_GRAMMAR_DEPTH = 50

class DepthException(Exception):
    """
    This exception is raised when the maximum grammar depth has been tried and exceeded,
    with more solutions still desired.
    """
    pass


def solve(args):
    """
    Primary function of the engine module. This interprets the arguments and several solver options.  
    """
    infile_full_path = args.infile
    infile_name = os.path.basename(infile_full_path)
    infile_dirname = os.path.dirname(infile_full_path)
    # Create a .tmp folder in the same directory as the input file
    tmp_output_dirname = '.tmp'
    outfile_dirname = os.path.join(infile_dirname, tmp_output_dirname)
    os.makedirs(outfile_dirname, exist_ok=True)
    outfile_name = _get_outfile_name(infile_name)
    outfile_full_path = os.path.join(outfile_dirname, outfile_name)

    sygus_to_smt_options = dict()
    sygus_to_smt_options['additional_constraints'] = []
    # Starting grammar_depth value; this will increment on each `unsat` until MAX_GRAMMAR_DEPTH is tried
    sygus_to_smt_options['grammar_depth'] = args.starting_depth
    solver_call_options = dict()
    solver_call_options['smtsolver'] = args.smtsolver

    # Loop until number of solutions is reached
    # Calculate loop condition based on arguments pertaining to multiple solutions
    solution_number = 1
    while args.stream or (solution_number <= args.num_solutions):
        grammars = sygus_to_smt(infile_full_path, outfile_full_path, sygus_to_smt_options)
        solver_result = call_solver(outfile_full_path, grammars, solver_call_options)
        if solver_result == 'unsat':
            if sygus_to_smt_options['grammar_depth'] < MAX_GRAMMAR_DEPTH:
                # If unsat but grammar depth can be incremented, do so and run again
                sygus_to_smt_options['grammar_depth'] += 1
            else:
                # Raise exception if grammar depth cannot be incremented
                print(solver_result)
                raise DepthException('Maximum grammar depth {} exceeded.'.format(MAX_GRAMMAR_DEPTH))
                exit(0)
        elif solver_result == 'unknown':
            print(solver_result)
            exit(0)
        else:
            pretty_solution_string, solution_as_constraint = solver_result
            print('sat')
            print(pretty_solution_string)
            # Append the negation of the solution in order to dismiss it from the next round of synthesis
            sygus_to_smt_options['additional_constraints'].append('(not {})'.format(solution_as_constraint))
            solution_number = solution_number + 1


def _get_outfile_name(infile_name):
    """
    Generate SMT filename based on input filename.  
    :param infile_name: string  
    :return: string  
    """
    dot_index = infile_name.rfind('.')
    outfile_name = '{}.smt2'.format(infile_name[:dot_index])
    return outfile_name