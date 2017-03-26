'''
This program checks extents(from starting point till ending point) of various
components of the program. Components include: functions, loops, conditionals,
structs, etc.
'''
import re

from store import counterparts, root
from utilities import statement


possible_function_list = [
        'blank', 'comment1', 'preprocessor',
        'function_prototype', 'function_definition', 'forloop', 'whileloop',
        'dowhileloop', 'ifcondition', 'elseifcondition', 'elsecondition',
        'switch', 'declaration', 'assignment', 'struct'
]

def process_line(lines_list, index):
    '''
    processes line according to defined function for particular type
    then returns line number, where counter_part of this line ends
    '''
    current_line = lines_list[index]
    inst = statement(current_line, index)
    statement_type = inst.resolve()
    returned = eval(statement_type +_'(lines_list, index)')
    return returned


def blank(lines_list, index):
    return index


def comment1(lines_list, index):
    return index

def comment2(lines_list, index):
    for i in xrange(index, len(lines_list)):
        if '*/' in lines_list[i]:
            return i
    return len(lines_list)-1  # This won't have to execute

def preprocessor(name, lines_list, index):
    '''
    Function returns index of the ending line of the preprocessor
    '''
    if index == len(lines_list): return index
    one_liners = ['define', 'include', 'line', 'pragma']
    if name in one_liners:
        return index
    if statement(lines_list[index]).is_preprocessor():
        thisname = re.search(r'\#(?P<name>\w+)', ).group('name')
        if thisname == counterparts[name]:
            return index
        thisend = preprocessor(thisname, lines_list, index)
        return preprocessor(name, lines_list, thisend+1)
    else:
        thisend = process_line(lines_list, index)
        return preprocessor(name, lines_list, thisend+1)


def function_prototype(lines_list, index):
    '''
    yet to handle comma separated prototypes
    '''
    for i in xrange(index, len(lines_list)):
        if re.search(r'\)\s*?;', lines_list[i]):
            return i
    return len(lines_list)-1


def function_definition(lines_list, index):
    '''
    yet to handle strange cases or double quotes spoilers
    '''
    ocount = lines_list[index].count('{')
    ccount = lines_list[index].count('}')
    if ccount > ocount:
        return index
    thisend = process_line(lines_list, index)
    return function_definition(lines_list, thisend+1)

