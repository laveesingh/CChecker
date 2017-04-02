import argparse
import os
import sys

import util.colors as colors
from util.store import *
from util import helper, program

import specs as specmod

# disable creation of *.pyc files
sys.dont_write_bytecode = True

def check_args(parser, args):
    '''This function will parse the arguments and make sure the arguments
    passed are correct and complete.'''

    #TODO: add more exceptions here (required)
    #TODO: add an error class (Low priority)

    #if not args.dir and not args.file:
    #    raise Exception(colors.FAIL + "You have to mention either directory or files" +
    #            colors.ENDC)

    if not args.file and not args.dir:
        raise Exception(colors.FAIL + "You must mention either -f or -d " + 
                colors.ENDC)

    #if args.file and args.dir:
    #    raise Exception(colors.FAIL + "Can't use both -f and -d " + 
    #            colors.ENDC)

    if args.dir and not os.path.isdir(args.dir):
        raise Exception(colors.FAIL + "Directory not found: " + str(args.dir) +
                colors.ENDC)

    if args.file and not os.path.isfile(args.file):
        raise Exception(colors.FAIL + "File not found: " + str(args.file) +
                colors.ENDC)

    if args.spec != 'all' and args.list:
        raise Exception(colors.FAIL + "You can't use both -s and -l: " +
                colors.ENDC)

    if args.spec != 'all' and not os.path.isfile(args.spec):
        raise Exception(colors.FAIL + "File not found: " + str(args.spec) +
                colors.ENDC)

def parse_specs(spec_file, spec_list):
    '''This function will parse the spec file and return a list of
    check numbers which are required to perform.'''
    if spec_list:
        return map(int, spec_list.split(" "))
    name = []
    if spec_file == 'all':
        name = [x for x in range(1,26)]
    else:
        lines = [line for line in open(spec_file, 'r+').read().split('\n') if line.strip()]
        for line in lines:
            # We have assumed the current spec file to be like a spec number per line
            # though we can and we need to make this parser more smart and decide on
            # various formats which can be there
            try:
                name.extend(map(int,line.split()))
            except ValueError:
                raise Exception("Unable to parse specification file due to its invalid bad format")
    return name

def eval_specs(pinst, specs_list):
    '''This function will accept a list of specification numbers and call the related functions'''

    for spec_no in specs_list:
        fname = specmod.num_to_name[spec_no]
        try:
            getattr(specmod, fname)(pinst)
        except AttributeError:
            raise #Exception("The source code sucks")

def eval_dir(dirname, specs):
    ''''''
    if not os.path.isdir(dirname):
        print "Man this code sucks!"

    files = os.listdir(dirname)
    for file in files:
        if os.path.isdir(file):
            eval_dir(file, specs)
        if file.endswith('.c'):
            pinst = program.program()
            pinst.load_attrs(open(file), 'r+')
            eval_specs(pinst, specs)

if __name__ == '__main__':
    helptext = "A program to test your C programs for coding violations which may lead to runtime errors and unexpected results."
    parser = argparse.ArgumentParser(description=helptext)
    parser.add_argument('-s', '--spec',
                    help="Specification file containing checks", default='all')
    parser.add_argument('-f', '--file', help="C input file to be checked")
    #parser.add_argument('-d', '--dir', help="Directory containing C files")
    parser.add_argument('-l', '--list', help="List of specs from command line")
    parser.add_argument('-d', '--dir', help="Directory containing C files")
    #parser.add_argument('html', help="Show output in html")
    #parser.add_argument('lspec', help="Show the spec file")
    args = parser.parse_args()
    # If there's any error with provided input files
    check_args(parser, args)
    #print args
    specs = parse_specs(args.spec, args.list)
    if args.file:
        pinst = program.program()
        pinst.load_attrs(open(args.file, 'r+'))
        eval_specs(pinst, specs)
    if args.dir:
        eval_dir(args.dir, specs)

    res_dic = specmod.error_dic
    opname = args.file[:-2] + '.html'
    opfile = open(opname, 'w+')
    lno = 0
    was_nl = True
    tno = 0
    headb = "<html><head><title>CChecker</title></head><body><p style=\"font-size:20px\">"
    opfile.write(headb + '\n <pre>')
    #opfile.write("Total number of violations found are %d" % )
    for lines in open(args.file, 'r').readlines():
        #opfile.write('<pre></pre>')
        lno = lno + 1
        res_line = res_dic.get(lno)
        if res_line is None:
            opfile.write(lines)
            continue
        if lines.endswith('\n'):
            lines = lines[:-1]
            was_nl = True

        tno += len(res_line)
        ctag = "<font color = \"red\">"
        nline = "/*This line fails check no " + str(res_line) + " */ </font>"
        #print nline, lines
        opfile.write(ctag + lines + '        ' + str(nline))
        if was_nl:
            opfile.write('\n')

    opfile.write("<font color = \"blue\">Total number of violations found = %d</font>" % tno)
    for a in xrange(1, len(specmod.no_of_error))
    opfile.write('</p></pre></body></html>') 

    if args.html:
        os.system("xdg-open "+opname)
    opn = args.file[:-2] + '.opd'
    opf = open(opn, 'w+')
    for lineno in sorted(specmod.error_dic):
        opf.write(str(lineno) + " : " + str(specmod.error_dic[lineno]) + "\n")
    opf.close()
    #vars_dict = helper.parse_vars(pinst)
    #assign_list = helper.conditions(pinst)
    #uncomment the below line when we starts parsing loop variables
    #helper.comparison_floating(pinst)
    # helper.parse_function_calls(pinst)
    # helper.check_recursion(pinst)
    # helper.parse_comments(pinst)
    # helper.parse_switch(pinst)
    # helper.function_declaration(pinst)
    #helper.no_star_comments(pinst)
    #opf.write("Preprocessors = ")
    #for obs in pinst.preprocessors:
    #    opf.write(''.join(obs.text))
    #opf.write("\nFunctions = ")
    #for obs in pinst.functions:
    #    opf.write(''.join(obs.text))
    #    opf.write("Variables = " + str(obs.vars) + "\n")
    #    opf.write("Assignment in conditions = " + str(obs.assignments_in_cond) + "\n")
    #    opf.write("Comments in fn's = " + str(obs.comments) + "\n")
    #opf.write("\nStruct = ")
    #for obs in pinst.structs:
    #    opf.write(''.join(obs.text))
    #opf.write("\nComments = ")
    #for obs in pinst.global_comments:
    #    opf.write(''.join(obs.text))
    #opf.write("\nFunctions Proto = ")
    #for obs in pinst.func_prototypes:
    #    opf.write(''.join(obs.text))
    #opf.write("\nGlobal Var = ")
    #for obs in pinst.global_vars:
    #    opf.write(''.join(obs.text))
    #opf.write("\nUnion = ")
    #for obs in pinst.unions:
    #    opf.write(''.join(obs.text))
    #opf.write("\nUnrecognised = ")
    #for obs in pinst.unrecognized:
    #    opf.write(obs)
    opfile.close()
    #opf.close()

    #if oldname and fileEquals(opname, oldname):
    #    pass
    #print(pinst.lines)
