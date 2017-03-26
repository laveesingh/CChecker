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


	def preprocessor(lineno):
		''''''
		if is_preprocessor(self.lines[lineno]):
			pass

		return lineno

	def global_vars(lineno):
		''''''
		if is_global_var(self.lines[lineno]):
			pass

		return lineno

	def function(lineno):
		''''''
		if is_func(self.lines[lineno]):
			pass

		return lineno

	def func_prototype(lineno):
		''''''
		if is_func_prototype(self.lines[lineno]):
			pass

		return lineno

	def struct(lineno):
		''''''
		if is_struct(self.lines[lineno]):
			pass

		return lineno