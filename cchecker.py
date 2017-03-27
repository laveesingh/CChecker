import argparse
import os
import sys

import specs
import util.colors as colors
from util.store import *
from util import program

# disable creation of *.pyc files
sys.dont_write_bytecode = True

def check_args(parser, args):
    '''This function will parse the arguments and make sure the arguments
    passed are correct and complete.'''

    #TODO: add more exceptions here (required)
    #TODO: add an error class (Low priority)
    if not os.path.isfile(args.file):
        raise Exception(colors.FAIL + "File not found: " + str(args.file) +
                colors.ENDC)

    if args.spec != 'all' and not os.path.isfile(args.spec):
        raise Exception(colors.FAIL + "File not found: " + str(args.spec) +
                colors.ENDC)

def parse_specs(spec_file):
    '''This function will parse the spec file and return a list of
    check numbers which are required to perform.'''

    specs = []
    if spec_file == 'all':
        specs = [x for x in range(1,26)]
    else:
        lines = open(spec_file, 'r+').read()
        for line in lines:
            # We have assumed the current spec file to be like a spec number per line
            # though we can and we need to make this parser more smart and decide on
            # various formats which can be there
            try:
                specs.append(list(map(int,line.split(' '))))
            except ValueError:
                raise Exception("Unable to parse specification file due to its invalid bad format")
    return specs

def eval_specs(specs_list):
    '''This function will accept a list of specification numbers and call the related functions'''
    for spec_no in specs_list:
        fname = specs.num_to_name[spec_no]
        try:
            getattr(specs, fname)()
        except AttributeError:
            raise Exception("The source code sucks")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--spec',
                    help="Specification file of rules", default='all')
    parser.add_argument('-f', '--file', help="C input file", required=True)
    args = parser.parse_args()
    # If there's any error with provided input files
    check_args(parser, args)
    specs = parse_specs(args.spec)
    pinst = program.program()
    pinst.load_attrs(open(args.file, 'r+'))
    opname = args.file[:-2] + '.OP'
    open(opname, 'w').close()    
    opf = open(opname, 'w+')
    prepoptext = ''
    for obs in pinst.preprocessors:
        prepoptext = prepoptext + obs.text
    funtext = ''
    for obs in pinst.functions:
        funtext = funtext + obs.text
    strtext = ''
    for obs in pinst.structs:
        strtext = strtext + obs.text
    gctext = ''
    for obs in pinst.global_comments:
        gctext = gctext + obs.text
    fptext = ''
    for obs in pinst.func_prototypes:
        fptext = fptext + obs.text
    gvtext = ''
    for obs in pinst.global_vars:
        gvtext = gvtext + obs.text
    untext = ''
    for obs in pinst.unrecognized:
        untext = untext + obs
    opf.write("Preprocessors = " + prepoptext)
    opf.write('\n')
    opf.write("Functions = " + funtext)
    opf.write('\n')
    opf.write("Struct = " + strtext)
    opf.write('\n')
    opf.write("Functions Proto = " + fptext)
    opf.write('\n')
    opf.write("Comments = " + gctext)
    opf.write('\n')
    opf.write("Global Var = " + gvtext)
    opf.write('\n')
    opf.write("Unrecognised = " + untext)
    opf.close()
    #print(pinst.lines)

