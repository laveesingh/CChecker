import re
import sys

import myregex
import store
import parse

before_pattern = r'(?P<before>.*?)'
after_pattern = r'(?P<after>.*?)'

# disable creation of *.pyc files
sys.dont_write_bytecode = True

def is_blank(lines, lineno):
    '''
        For this line to be blank, it should contain, spaces and newline
        characters
    '''
    return not lines[lineno]

def is_forloop(lines, lineno):
    '''
        For this line to be a for loop, it has to follow the pattern:
        >>> for(init; condition; increment){
                body
            }
        Or the pattern:
        >>> for(init; condition; increment)
        {
            body
        }
    '''
    regex = r'for\s*\(.*\)\s*[\n\{]'
    if re.search(regex, lines[lineno]):
        return True
    return False

def is_whileloop(lines, lineno):
    '''
        For this line to be while loop, it has to follow the pattern:
        >>> while(condition){
                body
            }
        Or the pattern:
        >>> while(condition)
            {
                body
            }
    '''
    regex = r'while\s*\(.*\)\s*[\n\{]'
    if re.search(regex, lines[lineno]):
        return True
    return False

def is_dowhileloop(lines, lineno):
    '''
    For this line to be dowhileloop, it has to follow the pattern:
    >>> do{
            body
        } 
    '''
    regex = r'[^\w]do[^\w]'
    if re.search(regex, lines[lineno]):
        return True
    return False

def is_if(lines, lineno):
    '''
        For this line to be if condition, it has to follow the pattern:
        >>> if(condition){
                body
            }
        Or the pattern:
        >>> if(condition)
            {
                body
            }
    '''
    regex = r'if\s*\(.*\)\s*[\n\{]'
    if re.search(regex, lines[lineno]):
        return True
    return False

def is_elseif(lines, lineno):
    '''
        For this line to be else if, it has to follow the pattern:
        >>> else if(condition){
                body
            }
        Or the pattern:
        >>> else if(condition)
            {
                body
            }
    '''
    regex = r'else if\s*\(.*\)\s*[\n\{]'
    if re.search(regex, lines[lineno]):
        return True
    return False

def is_else(lines, lineno):
    '''
        For this line to be else, it has to follow the pattern:
        >>> else(condition){
                body
            }
        Or the pattern:
        >>> else(condition)
            {
                body
            }
    '''
    regex = r'else\s*\(.*\)\s*[\n\{]'
    if re.search(regex, lines[lineno]):
        return True
    return False

def is_switch(lines, lineno):
    '''
        For this line to be switch, it has to follow the pattern:
        >>> switch(condition){
                body
            }
        Or the pattern:
        >>> switch(condition)
            {
                body
            }
    '''
    regex = r'switch\s*\(.*\)\s*[\n\{]'
    if re.search(regex, lines[lineno]):
        return True
    return False

def is_declaration(lines, lineno):
    '''
        For this line to be only declaration of variable, it has to follow the
        pattern:
        >>> datatype var_name;
        Or the pattern:
        >>> datatype var1, var2, var3...;
    '''
    regex = r'((const)|(static))?\s*((void)|(int)|(float)|(char))\s*(?P<name>(\w+)\,?)\s*;'
    if re.search(regex, lines[lineno]):
        return True
    return False

def is_assignment(lines, lineno):
    '''
    For this line to be assignment, it has to follow the pattern:
    >>> datatype var_name = val;
    sor
    >>> datatype var1 = val1, var2 = val2;
    or
    >>> var_name = val;
    or
    >>> var1 = val1, var2 = val2;
    '''
    regex = r'[^=]\=[^=]'
    if myregex.search_wq(regex, lines[lineno]):
        return True
    return False

def is_union(lines, lineno):
    '''
    For this line to be union, it has to follow the pattern:
    >>> union name{
            body
        };
    >>> typedef union name{
            body
        };
    '''
    regex = r'union\s+\w+'
    if re.search(regex, lines[lineno]):
        return True
    return False

def resolve(lines, lineno):
    '''
    This function will resolve the type of the given line.
    '''
    if is_blank(lines, lineno): return 'blank'
    if parse.is_global_comments(lines, lineno): return 'comment1'
    if parse.is_preprocessor(lines, lineno): return 'preprocessor'
    if parse.is_func_proto(lines, lineno): return 'function_prototype'
    if parse.is_function(lines, lineno): return 'function_definition'
    if is_forloop(lines, lineno): return 'forloop'
    if is_whileloop(lines, lineno): return 'whileloop'
    if is_dowhileloop(lines, lineno): return 'dowhileloop'
    if is_if(lines, lineno): return 'ifcondition'
    if is_elseif(lines, lineno): return 'elseifcondition'
    if is_else(lines, lineno): return 'elsecondition'
    if is_switch(lines, lineno): return 'switch'
    if is_declaration(lines, lineno): return 'declaration'
    if is_assignment(lines, lineno): return 'assignment'
    if parse.is_struct(lines, lineno): return 'struct'
    if is_union(lines, lineno): return 'union'
    return 'screwed'
