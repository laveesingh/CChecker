import sys

# disable creation of *.pyc files
sys.dont_write_bytecode = True

num_to_name = {
	1: 'imp_type_conv',
	2: 'evaluate_diff_sidewise',
	3: 'bitwise_op',
	4: 'assignments_in_conditions',
	5: 'comparing_floats',
	6: 'gvar_as_fnpar',
	7: 'check_init',
	8: 'goto_continue',
	9: 'allocs',
	10: 'recursion',
	11: 'comments_style',
	12: 'code_commented',
	13: 'seq_in_comment',
	14: 'identifiers_scoping',
	15: 'proto_decl',
	16: 'sizeof_effects',
	17: 'rhshift_limits',
	18: 'unarymin_on_unsigned',
	19: 'loop_iterator',
	20: 'else_check',
	21: 'pointer_levels',
	22: 'unions',
	23: 'unreachable',
	24: 'default_check',
	25: 'booleans_switch',
}

def imp_type_conv():
	'''There should not be implicit type conversions between integer and floating point types, signed and unsigned types.'''
	pass

def evaluate_diff_sidewise():
	'''Statements that evaluate differently left to right and right to left should not be allowed. eg: statements like a = b[j] + j++;'''
	pass

def bitwise_op():
	'''Bitwise operations are not allowed on signed data types.'''
	pass

def assignments_in_conditions():
	'''Assignment statements in expressions resulting in Boolean value are not allowed. eg: if( b = a)'''
	pass

def comparing_floats():
	'''Equalities (==) and inequalities (<=, >=) between floating point values are not allowed.'''
	pass

def gvar_ar_fnpar():
	'''Global variables are not allowed as function parameters.'''
	pass

def check_init():
	'''Automatic (local) variables should have a value before they are used.'''
	pass

def goto_continue():
	'''goto and continue statements should not be used.'''
	pass

def allocs():
	'''Dynamic heap memory allocation should not be used. Hence functions such as malloc, calloc, realloc, free should not be used.'''
	pass

def recursion():
	'''There should not be any recursion.'''
	pass

def comments_style():
	'''There should not be any // style comments. All comments should be of the form /* ... */'''
	pass

def code_commented():
	'''Sections of code should not be commented out.'''
	pass

def seq_in_comment():
	'''Inside a comment, the character sequence /* should not be used.'''
	pass

def identifiers_scoping():
	'''Identifier in an inner scope should not have the same name as an identifier
	in an outer scope, and hide the identifier in the outer scope.'''
	pass

def proto_decl():
	'''All functions shall have prototype declarations that are visible at both function definition and function call.'''
	pass

def sizeof_effects():
	'''sizeof operator should not be used on expressions with side effect. Eg: sizeof(x=10) is not allowed, as this will not set x to 10.'''
	pass

def rhshift_limits():
	'''Right-hand operand of shift operator should lie between zero and one less than the width in bits of the left-hand side operand.
	Eg: x << 9 is not permitted if x is of width 8-bits.'''
	pass

def unarymin_on_unsigned():
	'''Unary minus operator should not be used on an expression whose type is unsigned.'''
	pass

def loop_iterator():
	'''Numeric variable used in a for loop for controlling loop iterations shall not be modified inside the loop.
	Eg: for(i=0; i<10; i++) {...i=i+3; ...} is not allowed.'''
	pass

def else_check():
	'''All if...else if... constructs should be terminated with an else clause.'''
	pass

def pointer_level():
	'''More than two levels of pointer indirection should not be used.'''
	pass

def unions():
	'''Unions should not be used.'''
	pass

def unreachable():
	'''There shall not be any unreachable code (code which will not be executed under any circumstances
	and which can be detected at compile-time).'''
	pass

def default_check():
	'''All switch statements should have a default clause.'''
	pass

def booleans_switch():
	'''A switch expression should not be effectively Boolean. Eg: switch(x==10) should not be used,
	as x==10 is effectively Boolean.'''
	pass
