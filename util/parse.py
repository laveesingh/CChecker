'''This module contains functions which will be parsing the text
and returning the end points of various components such as functions,
preprocessors, etc.'''

def preprocessor(lines, lineno):
	''''''
	pass

def function(lines, lineno):
	''''''
	pass

def global_var(lines, lineno):
	pass

def func_proto(lines, lineno):
    '''
    handles only inline function prototypes of the format
    >>> rettype func(args);
    '''
    return lineno + 1

def struct(lines, lineno):
	pass

def global_comments(lines, lineno):
	''''''
	if lines[lineno].startswith('//'):
		return lineno + 1

	else if lines[lineno].startswith('/*'):
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
    regex = r'((?P<ret>[a-zA-Z_]\w*)\*?\s+\*?(?P<name>[a-zA-Z_]\w*)\s*' +\
        r'\(.*\)\s*\[\n\{])'
    if re.search(regex, lines[lineno]):
        return True
    return False

def is_global_var(lines, lineno):
	pass

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