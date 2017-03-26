import sys

'''This file contains the class 'program' which will be representative
of the c program. This class will have objects of other classes as
attributes which represents various parts of the code.'''

# disable creation of *.pyc files
sys.dont_write_bytecode = True

class program:

	def __init__(self):
		self.functions = []
		self.macros = []
		self.structs = []
		self.global_vars = []
		self.proto_decl = []
		self.global_comments = []

	def load_attrs(self, fp):
		text = fp.read()
		list_of_lines = []
		for line in text:
			list_of_lines.append(line)

		lineno = 0
		no_of_lines = len(list_of_lines)

		while lineno < list_of_lines:
			
			if list_of_lines[lineno].strip() == '':
				lineno = lineno + 1
				continue

			lineno = preprocessor(list_of_lines, lineno)
			lineno = global_vars(list_of_lines, lineno)
			lineno = struct(list_of_lines, lineno)
			lineno = func_prototype(list_of_lines, lineno)
			lineno = function(list_of_lines, lineno)


def preprocessor(lines, lineno):
	''''''
	if is_preprocessor(lines[lineno]):
		pass

	return lineno

def global_vars(lines, lineno):
	''''''
	if is_global_var(lines[lineno]):
		pass

	return lineno

def function(lines, lineno):
	''''''
	if is_func(lines[lineno]):
		pass

	return lineno

def func_prototype(lines, lineno):
	''''''
	if is_func_prototype(lines[lineno]):
		pass

	return lineno

def struct(lines, lineno):
	''''''
	if is_struct(lines[lineno]):
		pass

	return lineno