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
		pass
