'''This module contains functions which will be parsing the text
and returning the end points of various components such as functions,
preprocessors, etc.'''

import re

from . import extents, utilities

def preprocessor(lines, lineno):
    ''''''
    #print lines[lineno]
    name = re.split(' |<', lines[lineno])[0]
    #name = lines[lineno].split(' |<')[0]
    name = name[1:]
    #print name
    return extents.preprocessor(name, lines, lineno)

def function(lines, lineno):
    ''''''
    no_of_cbraces = 0
    if '{' in lines[lineno]:
        no_of_cbraces = 1

    linep = lineno +1

    while True:
        #print lines[linep]
        no_of_cbraces += lines[linep].count('{')
        #print "New" + str(no_of_cbraces)
        no_of_cbraces -= lines[linep].count('}')
        #print "Closed" + str(no_of_cbraces)
        if no_of_cbraces == 0 or linep == len(lines) - 1:
            print linep
            return linep
        linep += 1     
    print no_of_cbraces, lines[lineno]


def global_var(lines, lineno):
	return extents.declaration(lines, lineno)

def func_proto(lines, lineno):
    '''
    handles only inline function prototypes of the format
    >>> rettype func(args);
    '''
    return lineno

def struct(lines, lineno):
    ''''''
    no_of_cbraces = 0
    if '{' in lines[lineno]:
        no_of_cbraces = 1

    linep = lineno +1

    while True:
        #print lines[linep]
        no_of_cbraces += lines[linep].count('{')
        #print "New" + str(no_of_cbraces)
        no_of_cbraces -= lines[linep].count('}')
        #print "Closed" + str(no_of_cbraces)
        if no_of_cbraces == 0 or linep == len(lines) - 1:
            print linep
            return linep
        linep += 1     
    print no_of_cbraces, lines[lineno]

def global_comments(lines, lineno):
	''''''
	if lines[lineno].startswith('//'):
		return lineno

	elif lines[lineno].startswith('/*'):
	    for i in xrange(index, len(lines_list)):
	        if '*/' in lines_list[i]:
	            return i
	    return len(lines_list)-1  # This won't have to execute		

	return lineno

def is_preprocessor(lines, lineno):
	'''
		For this line to be a preprocessor, it has to follow the pattern:
	    >>> #include something
	    >>> #define something
	    or some other preprocessor
	'''
	#TODO: improve this regex
	regex = r'\#((include)|(define)).*'
	if re.search(regex, lines[lineno]):
	    return True
	return False

def is_function(lines, lineno):
    '''
        For this line to be a function definition, it has to follow the
        pattern:
        >>> return_type function_name(type1 arg1...) {
                definition
            }
        Or the pattern:
        >>> return_type function_name(type1 arg1...)
        {
                definition
        }
        1. It starts at a return type, built in or self defined. This is
        followed by one or more spaces.
        2. Then comes the function name followed by parantheses
        3. There may be zero of more space characters between function name and
        the parantheses.
        4. Parantheses contain argument list, closing parantheses is followed
        by a { or newline;
    '''
    regex = r'(?P<type>(int)|(void)|(double)|(float)|(char))\s+(?P<name>(\w+))\((?P<arg>(.*))\)\s*'
    if re.search(regex, lines[lineno]):
        print lines[lineno]
        return True
    return False

def is_global_var(lines, lineno):
	return utilities.is_declaration(lines, lineno)

def is_func_proto(lines, lineno):
    '''
        For this line to be a function prototype, it has to follow the pattern:
        >>> return_type function_name(type1 arg1...);
        1. It starts at a return type, built in or self defined. This is
        followed by one or more spaces.
        2. Then comes the function name followed by parantheses
        3. There may be zero of more space characters between function name and
        the parantheses.
        4. Parantheses contain argument list, closing parantheses is followed
        by a semicolon;
    '''
    regex = r'((?P<ret>[a-zA-Z_]\w*)\*?\s+\*?(?P<name>[a-zA-Z_]\w*)\s*' +\
        r'\(.*\)\s*\;)'
    if re.search(regex, lines[lineno]):
        return True
    return False

def is_struct(lines, lineno):
    '''
    For this line to be struct, it has to follow the pattern:
    >>> struct name{
            body
        };
    >>> typedef struct name{
            body
        };
    '''
    regex = r'struct\s+\w+'
    if re.search(regex, lines[lineno]):
        return True
    return False

def is_global_comments(lines, lineno):
    '''
        Inline comment: // type
        There can be two patterns, either line starts with //
        or line contains comment after some statement/expression.
        But here we're looking, if line starts with comment

        Multiline comment: /* ... */ type
    '''	
    return lines[lineno].startswith('//') or lines[lineno].startswith('/*')