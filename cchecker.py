import argparse
import os

import utilities.colors as colors
from utilities.Store import *

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


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--spec',
                    help="Specification file of rules", default='all')
parser.add_argument('-f', '--file', help="C input file", required=True)
args = parser.parse_args()

### If there's any error with provided input files
check_args(parser, args)

flags_data = open(args.spec, 'r+').read()