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
	pass

def struct(lines, lineno):
	pass

def global_comments(lines, lineno):
	pass

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
	pass

def is_global_var(lines, lineno):
	pass

def is_func_proto(lines, lineno):
	pass

def is_struct(lines, lineno):
	pass

def is_global_comments(lines, lineno):
	pass