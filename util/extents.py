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
    handles only inline function prototypes of the format
    >>> rettype func(args);
    '''
    return index


def function_definition(lines_list, index):
    '''
    handles only function of the format
    >>> rettype func(args){
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return function_definition(lines_list, thisend+1)


def forloop(lines_list, index):
    '''
    handles only for loops of the format
    >>> for(details){
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return forloop(lines_list, thisend+1)


def whileloop(lines_list, index):
    '''
    handles only while loops of the format
    >>> while(conditions){
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return whileloop(lines_list, thisend+1)

def dowhileloop(lines_list, index):
    '''
    handles only dowhile loops of the format
    >>> do{
            body
        } while(condition);
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return dowhileloop(lines_list, thisend+1)

def ifcondition(lines_list, index):
    '''
    handles only if conditions of the format
    >>> if(conditions){
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return ifcondition(lines_list, thisend+1)


def elseifcondition(lines_list, index):
    '''
    handles only else if conditions of the format
    >>> else if(conditions){
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return elseifcondition(lines_list, thisend+1)


def elsecondition(lines_list, index):
    '''
    handles only else conditions of the format
    >>> else{
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return elsecondition(lines_list, thisend+1)


def switch(lines_list, index):
    '''
    handles only switch of the format
    >>> switch(constraint){
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return switch(lines_list, thisend+1)


def struct(lines_list, index):
    '''
    handles only structs of the format
    >>> struct name{
            body
        };
    '''
    if lines_list[index].strip() == '};':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return struct(lines_list, thisend+1)

def declaration(lines_list, index):
    '''handles only declarations of the following format
    >>> datatype var1;
    or
    >>> datatype var1, var2...;
    '''
    return index

def assignment(lines_list, index):
    '''handles only assignments of the following format
    >>> datatype var1 = val1;
    or any other inline assignment
    '''
    return index
