import sys

import util.helper as helper

# disable creation of *.pyc files
sys.dont_write_bytecode = True

error_dic = {}
no_of_errors = [0 for a in xrange(0, 26)]

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

def imp_type_conv(pinst):
	'''There should not be implicit type conversions between integer and floating point types, signed and unsigned types.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	res = helper.check_implicit_type_conversion(pinst)
	if not res:
		return
	for line in res:
		no_of_errors[1] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(1)

def evaluate_diff_sidewise(pinst):
	'''Statements that evaluate differently left to right and right to left should not be allowed. eg: statements like a = b[j] + j++;'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"

def bitwise_op(pinst):
	'''Bitwise operations are not allowed on signed data types.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	res = helper.bitwise_op(pinst)
	if not res:
		return
	for line in res:
		no_of_errors[3] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(3)

def assignments_in_conditions(pinst):
	'''Assignment statements in expressions resulting in Boolean value are not allowed. eg: if( b = a)'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	result = helper.conditions(pinst)
	if not result:
		return
	#print "Following lines have violated the check 4"
	for line in result:
		no_of_errors[4] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(4)

def comparing_floats(pinst):
	'''Equalities (==) and inequalities (<=, >=) between floating point values are not allowed.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	res = helper.comparison_floating(pinst)
	if not res:
		return
	for line in res:
		no_of_errors[5] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(5)

def gvar_as_fnpar(pinst):
	'''Global variables are not allowed as function parameters.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"

def check_init(pinst):
	'''Automatic (local) variables should have a value before they are used.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	result = helper.check_initialised_variable(pinst)
	if not result:
		return
	#print "Following lines have violated check 8"
	for line in result:
		no_of_errors[7] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(7)

def goto_continue(pinst):
	'''goto and continue statements should not be used.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	result = helper.find_goto(pinst)
	if not result:
		return
	#print "Following lines have violated check 8"
	for line in result:
		no_of_errors[8] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(8)

def allocs(pinst):
	'''Dynamic heap memory allocation should not be used. Hence functions such as malloc, calloc, realloc, free should not be used.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	result = helper.find_dynamic_memory_allocation(pinst)
	if not result:
		return
	#print "Following lines have violated check 9"
	for line in result:
		no_of_errors[9] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(9)

def recursion(pinst):
	'''There should not be any recursion.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	helper.parse_function_calls(pinst)
	res = helper.check_recursion(pinst)
	if not res:
		return
	for line in res:
		no_of_errors[10] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(10)

def comments_style(pinst):
	'''There should not be any // style comments. All comments should be of the form /* ... */'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	res = helper.single_comments(pinst)
	if not res:
		return
	for line in res:
		no_of_errors[11] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(11)


def code_commented(pinst):
	'''Sections of code should not be commented out.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"

def seq_in_comment(pinst):
	'''Inside a comment, the character sequence /* should not be used.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"

def identifiers_scoping(pinst):
	'''Identifier in an inner scope should not have the same name as an identifier
	in an outer scope, and hide the identifier in the outer scope.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"

def proto_decl(pinst):
	'''All functions shall have prototype declarations that are visible at both function definition and function call.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	res = helper.function_declaration(pinst)
	if not res:
		return
	for line in res:
		no_of_errors[15] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(15)

def sizeof_effects(pinst):
	'''sizeof operator should not be used on expressions with side effect. Eg: sizeof(x=10) is not allowed, as this will not set x to 10.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	res = helper.verify_sizeof(pinst)
	if not res:
		return
	for line in res:
		no_of_errors[16] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(16)

def rhshift_limits(pinst):
	'''Right-hand operand of shift operator should lie between zero and one less than the width in bits of the left-hand side operand.
	Eg: x << 9 is not permitted if x is of width 8-bits.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"

def unarymin_on_unsigned(pinst):
	'''Unary minus operator should not be used on an expression whose type is unsigned.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"

def loop_iterator(pinst):
	'''Numeric variable used in a for loop for controlling loop iterations shall not be modified inside the loop.
	Eg: for(i=0; i<10; i++) {...i=i+3; ...} is not allowed.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"

def else_check(pinst):
	'''All if...else if... constructs should be terminated with an else clause.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	res = helper.if_else(pinst)
	if not res:
		return
	for line in res:
		no_of_errors[20] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(20)

def pointer_levels(pinst):
	'''More than two levels of pointer indirection should not be used.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"

def unions(pinst):
	'''Unions should not be used.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	res = []
	if not pinst.unions:
		return
	for union in pinst.unions:
		no_of_errors[22] += 1
		line = union.start
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(22)

def unreachable(pinst):
	'''There shall not be any unreachable code (code which will not be executed under any circumstances
	and which can be detected at compile-time).'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"

def default_check(pinst):
	'''All switch statements should have a default clause.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	result = helper.parse_switch(pinst)
	if not result:
		return
	for line in result:
		no_of_errors[24] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(24)


def booleans_switch(pinst):
	'''A switch expression should not be effectively Boolean. Eg: switch(x==10) should not be used,
	as x==10 is effectively Boolean.'''
	func_name = sys._getframe().f_code.co_name
	#print func_name + "Not yet coded!"
	result = helper.check_switch_condition(pinst)
	if not result:
		return
	for line in result:
		no_of_errors[25] += 1
		if error_dic.get(line) is None:
			error_dic[line] = []
		error_dic[line].append(25)
