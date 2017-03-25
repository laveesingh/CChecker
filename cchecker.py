# STDLib imports
import argparse
import os

# Local imports
import specs
import util.colors as colors
from util.store import *

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
            # various fromats which can be there
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
    ### If there's any error with provided input files
    check_args(parser, args)
    specs = parse_specs(args.spec)
