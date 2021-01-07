"""
Module to handle reading files with SyGuS grammars and writing corresponding files
with constraint grammars.
"""

import subprocess, itertools, warnings
from src.SyGuSGrammar import load_from_string
from src.ConstraintGrammar import ConstraintGrammar
from src.lisplike import pretty_string

# Replace SyGuS grammars in file with constraint grammars in SMT-Lib format
def sygus_to_constraint(infile_name, outfile_name=None):
    """
    Write a copy of input file, replacing each SyGuS grammar by the corresponding
    constraint grammar in SMT-Lib format.
    :param infile_name: string
    :param outfile_name: string
    :return grammars: list [ConstraintGrammar]
    """
    if outfile_name is None:
        outfile_name = get_outfile_name(infile_name)
    grammars = []
    with open(infile_name) as infile:
        with open(outfile_name, 'w') as outfile:
            reading_sygus = False
            synthfun_str = ''
            depth = 0
            for num,line in enumerate(infile):
                # Read infile line-by-line
                if reading_sygus:
                    # SyGuS grammar is not written to the outfile
                    # Continue reading SyGuS grammar
                    # Only include uncommented portions into grammar
                    if ';' in line:
                        line = line[:line.find(';')]
                    synthfun_str += '\n' + line
                    depth += line.count('(') - line.count(')')
                    if depth <= 0:
                        # Done reading SyGus grammar
                        reading_sygus = False
                        # Process and write constraint grammar
                        grammar = load_from_string(synthfun_str)
                        constraint_grammar = ConstraintGrammar(grammar)
                        constraint_grammar.compute_constraint_encoding()
                        outfile.write(constraint_grammar.pretty_smt_encoding())
                        # Maintain constraint grammar
                        grammars.append(constraint_grammar)
                        synthfun_str = ''
                elif line[:11] == '(synth-fun ':
                    # Start reading SyGuS grammar into synthfun_str
                    reading_sygus = True
                    synthfun_str = line
                    depth = line.count('(') - line.count(')')
                else:
                    # Aside from grammars, infile and outfile should match
                    outfile.write(convert_to_smt(line))
    return grammars

def call_solver(smtfile_name, grammars):
    """
    Call SMT solver and, if sat, display grammar expressions corresponding to boolean
    valuations in returned SMT model.
    :param smtfile_name: string
    :param grammars: list [ConstraintGrammar]
    :return model: dict {string: bool}
    """
    # Call CVC4 solver on smtfile_name
    solver = 'cvc4'
    proc = subprocess.Popen('{} {} -m --lang=smt2'.format(solver, smtfile_name), shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    solver_out, err = proc.communicate()
    # Process output
    model = {}
    if solver_out == '' or 'error' in solver_out[:6]:
        if err:
            print(err)
        else:
            print(solver_out)
    else:
        solver_lines = solver_out.split('\n')
        if solver_lines[0] == 'sat':
            # Format SMT model
            for line in solver_lines:
                if 'define-fun' in line:
                    line = line.split(' ')
                    model[line[1]] = line[4][:-1] == 'true'
            print('sat')
            # Evaluate and print synthesized lemmas over SMT model
            for constraint_grammar in grammars:
                print(constraint_grammar.sygus_grammar.name)
                print(pretty_string(constraint_grammar.evaluate(model), noindent=True))
        else:
            print('unsat')
    return model

def convert_to_smt(line):
    """
    Convert a string into SMT format.
    For uncommented appearances, replace 'constraint' with 'assert'
    and 'check-synth' with 'check-sat'.
    :param line: string
    :return line: string
    """
    index = len(line)
    if ';' in line:
        index = line.find(';')
    if 'constraint' in line[:index]:
        line = line[:index].replace('constraint','assert') + line[index:]
    if 'check-synth' in line[:index]:
        line = line[:index].replace('check-synth','check-sat') + line[index:]
    return line

def get_outfile_name(infile_name):
    """
    Generate SMT filename based on input filename.
    Output file is located in an output folder in the input file directory.
    :param infile_name: string
    :param outfile_name: string
    """
    dot_index = infile_name.rfind('.')
    slash_index = infile_name.rfind('/')
    if slash_index == -1:
        slash_index = 0
        infile_name = '/' + infile_name
    outfile_name = ''.join([infile_name[:slash_index],'/output',
                            infile_name[slash_index:dot_index],'.smt'])
    return outfile_name