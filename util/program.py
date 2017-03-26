import sys

'''This file contains the class 'program' which will be representative
of the c program. This class will have objects of other classes as
attributes which represents various parts of the code.'''

# disable creation of *.pyc files
sys.dont_write_bytecode = True

class program:

	def __init__(self):
		self.functions = []
		self.preprocessors = []
		self.structs = []
		self.global_vars = []
		self.func_prototypes = []
		self.global_comments = []
		self.lines = []

	def load_attrs(self, fp):
		text = fp.read()
		for line in text:
			self.lines.append(line)

		lineno = 0
		no_of_lines = len(self.lines)

		while lineno < no_of_lines:
			
			if self.lines[lineno].strip() == '':
				lineno = lineno + 1
				continue

			lineno = preprocessor(lineno)
			lineno = global_vars(lineno)
			lineno = struct(lineno)
			lineno = func_prototype(lineno)
			lineno = function(lineno)
			lineno = global_comments(lineno)


	def preprocessor(lineno):
		'''It will check whether the given line is the beginning
		of a preprocessor or not. If it is the beginning it will do following
		things:
		1. Find the end(last line) of this preprocessor
		2. Make a object of preprocessor class
		3. Add that object to self.preprocessors list
		4. Return the line number next to where preprocessor ends

		If it's not the beginning of a preprocessor, then it will
		return the same line number which was passed.'''
		if is_preprocessor(self.lines[lineno]):
			pass

		return lineno

	def global_vars(lineno):
		'''It will check whether the given line is the beginning
		of declaration of a global var or not. If it is the beginning it will
		do the following things:
		1. Find the end(last line) of this declaration statement
		2. Make a object of global_vars class
		3. Add that object to self.global_vars list
		4. Return the line number next to where this statement ends

		If it's not the beginning of declaration of a global variable, then it
		will return the same line number which was passed.'''
		if is_global_var(self.lines[lineno]):
			pass

		return lineno

	def function(lineno):
		'''It will check whether the given line is the beginning
		of a function or not. If it is the beginning it will do following
		things:
		1. Find the end(last line) of this function
		2. Make a object of function class
		3. Add that object to self.functions list
		4. Return the line number next to where this function ends

		If it's not the beginning of a function, then it will
		return the same line number which was passed.'''
		if is_func(self.lines[lineno]):
			pass

		return lineno

	def func_prototype(lineno):
		'''It will check whether the given line is the beginning
		of a function prototype or not. If it is the beginning it will do following
		things:
		1. Find the end(last line) of this function prototype
		2. Make a object of func_prototype class
		3. Add that object to self.func_prototypes list
		4. Return the line number next to where this function prototype ends

		If it's not the beginning of a function prototype, then it will
		return the same line number which was passed.'''
		if is_func_prototype(self.lines[lineno]):
			pass

		return lineno

	def struct(lineno):
		'''It will check whether the given line is the beginning
		of a struct or not. If it is the beginning it will do following
		things:
		1. Find the end(last line) of this struct
		2. Make a object of struct class
		3. Add that object to self.structs list
		4. Return the line number next to where this struct ends

		If it's not the beginning of a struct, then it will
		return the same line number which was passed.'''
		if is_struct(self.lines[lineno]):
			pass

		return lineno

	def global_comments(lineno):
		'''It will check whether the given line is the beginning
		of a global comments or not. If it is the beginning it will do
		following things:
		1. Find the end(last line) of this global comments
		2. Make a object of global_comments class
		3. Add that object to self.global_comments list
		4. Return the line number next to where this global_comments ends

		If it's not the beginning of a global comments, then it will
		return the same line number which was passed.'''
		if is_global_comments(self.lines[lineno]):
			pass

		return lineno