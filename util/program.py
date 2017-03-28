'''This file contains the class 'program' which will be representative
of the c program. This class will have objects of other classes as
attributes which represents various parts of the code.'''

import sys

from . import parse

import components.function as function
import components.struct as struct
import components.preprocessor as preprocessor
import components.func_prototype as func_prototype
import components.global_var as global_var
import components.global_comment as global_comment

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
		# Make sure we track things which we are unable to parse
		self.unrecognized = []

	def load_attrs(self, fp):
		text = fp.readlines()
		for line in text:
			self.lines.append(line)

		lineno = -1
		no_of_lines = len(self.lines)

		while lineno < no_of_lines - 1:

			lineno = lineno + 1
			
			if self.lines[lineno].strip() == '':
				continue

			# The following sequence of calling function is trivial for now
			# and is like this for no reason. We surely want to improve on this
			# but is left as is because we are currently concentrating on the
			# implementation part. We need to revisit this while optimising.

			flag, lineno = self.fpreprocessor(lineno)
			if flag:
				continue
			flag, lineno = self.fglobal_vars(lineno)
			if flag:
				continue
			flag, lineno = self.fstruct(lineno)
			if flag:
				continue
			flag, lineno = self.ffunc_prototype(lineno)
			if flag:
				continue
			flag, lineno = self.ffunction(lineno)
			if flag:
				continue
			flag, lineno = self.fglobal_comments(lineno)
			if flag:
				continue
			self.unrecognized.append(self.lines[lineno])


	def fpreprocessor(self, lineno):
		'''It will check whether the given line is the beginning
		of a preprocessor or not. If it is the beginning it will do following
		things:
		1. Find the end(last line) of this preprocessor
		2. Make a object of preprocessor class
		3. Add that object to self.preprocessors list
		4. Return the line number next to where preprocessor ends

		If it's not the beginning of a preprocessor, then it will
		return the same line number which was passed.'''
		if parse.is_preprocessor(self.lines, lineno):
			endline = parse.preprocessor(self.lines, lineno)
			text = self.lines[lineno : endline + 1]
			pclass = preprocessor.preprocessor(text, [lineno, endline])
			self.preprocessors.append(pclass)
			return True, endline

		return False, lineno

	def fglobal_vars(self, lineno):
		'''It will check whether the given line is the beginning
		of declaration of a global var or not. If it is the beginning it will
		do the following things:
		1. Find the end(last line) of this declaration statement
		2. Make a object of global_vars class
		3. Add that object to self.global_vars list
		4. Return the line number next to where this statement ends

		If it's not the beginning of declaration of a global variable, then it
		will return the same line number which was passed.'''
		if parse.is_global_var(self.lines, lineno):
			endline = parse.global_var(self.lines, lineno)
			text = self.lines[lineno : endline + 1]
			gvclass = global_var.global_vars(text, [lineno, endline])
			self.global_vars.append(gvclass)
			return True, endline

		return False, lineno

	def ffunction(self, lineno):
		'''It will check whether the given line is the beginning
		of a function or not. If it is the beginning it will do following
		things:
		1. Find the end(last line) of this function
		2. Make a object of function class
		3. Add that object to self.functions list
		4. Return the line number next to where this function ends

		If it's not the beginning of a function, then it will
		return the same line number which was passed.'''
		if parse.is_function(self.lines, lineno):
			endline = parse.function(self.lines, lineno)
			text = self.lines[lineno : endline + 1]
			fclass = function.function(text, [lineno, endline])
			self.functions.append(fclass)
			return True, endline

		return False, lineno

	def ffunc_prototype(self, lineno):
		'''It will check whether the given line is the beginning
		of a function prototype or not. If it is the beginning it will do following
		things:
		1. Find the end(last line) of this function prototype
		2. Make a object of func_prototype class
		3. Add that object to self.func_prototypes list
		4. Return the line number next to where this function prototype ends

		If it's not the beginning of a function prototype, then it will
		return the same line number which was passed.'''
		if parse.is_func_proto(self.lines, lineno):
			endline = parse.func_proto(self.lines, lineno)
			text = self.lines[lineno : endline + 1]
			fpclass = func_prototype.func_prototype(text, [lineno, endline])
			self.func_prototypes.append(fpclass)
			return True, endline

		return False, lineno

	def fstruct(self, lineno):
		'''It will check whether the given line is the beginning
		of a struct or not. If it is the beginning it will do following
		things:
		1. Find the end(last line) of this struct
		2. Make a object of struct class
		3. Add that object to self.structs list
		4. Return the line number next to where this struct ends

		If it's not the beginning of a struct, then it will
		return the same line number which was passed.'''
		if parse.is_struct(self.lines, lineno):
			endline = parse.struct(self.lines, lineno)
			text = self.lines[lineno : endline + 1]
			sclass = struct.struct(text, [lineno, endline])
			self.structs.append(sclass)
			return True, endline

		return False, lineno

	def fglobal_comments(self, lineno):
		'''It will check whether the given line is the beginning
		of a global comments or not. If it is the beginning it will do
		following things:
		1. Find the end(last line) of this global comments
		2. Make a object of global_comments class
		3. Add that object to self.global_comments list
		4. Return the line number next to where this global_comments ends

		If it's not the beginning of a global comments, then it will
		return the same line number which was passed.'''
		if parse.is_global_comments(self.lines, lineno):
			endline = parse.global_comments(self.lines, lineno)
			text = self.lines[lineno : endline + 1]
			gcclass = global_comment.global_comments(text, [lineno, endline])
			self.global_comments.append(gcclass)
			return True, endline

		return False, lineno