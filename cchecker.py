import argparse
import os

import utilities.colors as colors
from utilities.Store import *

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--specification',
                    help="Specification file of rules")
parser.add_argument('-i', '--input', help="C input file")
args = parser.parse_args()

### If there's any error with provided input files
if args.specification is None:
    parser.print_help()
    raise Exception(colors.FAIL + "Specification file not given" +
            colors.ENDC)
if args.input is None:
    parser.print_help()
    raise Exception(colors.FAIL + "C input file not given" + colors.ENDC)

if not os.path.isfile(args.specification):
    raise Exception(colors.FAIL + "No such file: " + str(args.specification) +
            colors.ENDC)
if not os.path.isfile(args.input):
    raise Exception(colors.FAIL + "No such file: " + str(args.input) +
            colors.ENDC)

flags_data = open(args.specification, 'r+').read()

