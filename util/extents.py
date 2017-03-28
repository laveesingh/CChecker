'''
This program checks extents(from starting point till ending point) of various
components of the program. Components include: functions, loops, conditionals,
structs, etc.
'''
import re

from store import counterparts, root
import parse
import utilities

from components import (
        function as Function
)


possible_function_list = [
        'blank', 'comment1', 'preprocessor',
        'function_prototype', 'function_definition', 'forloop', 'whileloop',
        'dowhileloop', 'ifcondition', 'elseifcondition', 'elsecondition',
        'switch', 'declaration', 'assignment', 'struct', 'union'
]

def blank(lines_list, index):
    return index


def preprocessor(name, lines_list, index):
    '''
    Function returns index of the ending line of the preprocessor
    '''
    if index == len(lines_list): return index
    one_liners = ['define', 'include', 'line', 'pragma']
    #print name
    if name in one_liners:
        return index
    if parse.is_preprocessor(lines_list, index):
        thisname = re.search(r'\#(?P<name>\w+)', ).group('name')
        if thisname == counterparts[name]:
            return index
        thisend = preprocessor(thisname, lines_list, index)
        return preprocessor(name, lines_list, thisend+1)
    else:
        thisend = process_line(lines_list, index)
        return preprocessor(name, lines_list, thisend+1)


def function_prototype(lines_list, index, root_dict):
    '''
    For now it handles only cases of the pattern:
    >>> rettype funcname(parameter_list);
    '''
    pattern = r'(?P<type>\w+)\s+(?P<name>\w+)\s*\((?P<args>.*)\)'
    match = re.search(pattern, lines_list[index])
    rettype = match.group('type')
    funcname = match.group('name')
    args = match.group('args')
    arglist, varlist = fetch_arglist(args)  #only datatypes would be enough
    instance = Function(funcname, rettype, arglist)
    if root_dict.get(instance) is None:
        root_dict[instance] = {}
    root_dict[instance]['name'] = funcname
    root_dict[instance]['rettype'] = rettype
    root_dict[instance]['arglist'] = arglist
    root_dict[instance]['prototype'] = True
    root_dict[instance]['prototype_visible'] = False  # check at function definition construction 
    return index


def function_definition(lines_list, start_index, current_index, root_dict):
    '''
    handles only function of the format
    >>> rettype func(args){
            body
        }
    '''
    if current_index == start_index:
        pattern = r'(?P<type>\w+)\s+(?P<name>\w+)\s*\((?P<args>.*)\)'
        match = re.search(pattern, lines_list[current_index])
        rettype = match.group('type')
        funcname = match.group('name')
        args = match.group('args')
        arglist, varlist = fetch_arglist(args)  # need to create it, datatypes list, variables list
        instance = Function(funcname, rettype, arglist)
        if root_dict.get(instance) is None:
            root_dict[instance] = {}
            root_dict[instance]['name'] = funcname
            root_dict[instance]['rettype'] = rettype
            root_dict[instance]['arglist'] = arglist
        if root_dict[instance].get('prototype'):
            root_dict[instance]['prototype_visible'] = True
        else:
            root_dict[instance]['prototype_visible'] = False
        root_dict[instance]['start_index'] = start_index
        root_dict[instance]['varlist'] = varlist

    if lines_list[index].strip() == '}':  #ignored inline comments for now
        root_dict[instance]['end_index'] = current_index
        return current_index
    statement_type = utilities.resolve(lines_list, current_index)
    returned = eval(statement_type +'(lines_list, start_index, current_index, root_dict[instance])')  # Instance might not be here due to recursive step, need to take care of this
    return function_definition(lines_list, returned+1)


def forloop(lines_list, start_index, current_index, detail_dict):
    '''
    handles only for loops of the format
    >>> for(details){
            body
        }
    '''
    if current_index == start_index:
        pattern = r'for\s*\((?P<init>.*);(?P<cond>.*);(?P<step>.*)\)'
        match = re.search(pattern, lines_list[current_index])
        init = match.group('init')
        cond = match.group('cond')
        step = match.group('step')
        varlist = fetch_varlist(init)  # need to create it, variables list
        if detail_dict.get('forloops') is None:
            detail_dict['forloops'] = []
        detail_dict['forloops'].append({})
        cur_loop_index = len(detail_dict['forloops']) - 1
        detail_dict['forloops'][cur_loop_index]['varlist'] = varlist
        # TODO: Need further careful modification
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    statement_type = utilities.resolve(lines_list, current_index)
    returned = eval(statement_type +'(lines_list, start_index, current_index, detail_dict["forloops"][cur_loop_index])')  # cur_loop_index might not be here due to recursion, need to take care of this
    return forloop(lines_list, returned+1)


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

def union(lines_list, index):
    '''
    handles only structs of the format
    >>> union name{
            body
        };
    '''
    return index

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
