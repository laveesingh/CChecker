from util import utilities

line = raw_input("Enter the statement line: ")
line_number = 0

lineobject = util.statement(line, line_number)

print "Blank:", lineobject.isblank()
print "Inline comment:",lineobject.is_comment1()
print "Preprocessor:", lineobject.is_preprocessor()
print "function prototype:", lineobject.is_function_prototype()
print "function definition:", lineobject.is_function_definition()
print "for loop:", lineobject.is_forloop()
print "while loop:", lineobject.is_whileloop()
print "if condition:", lineobject.is_if()
print "else if condition:",lineobject.is_elseif()
print "else condition:",lineobject.is_else()
print "switch statement:",lineobject.is_switch()
print "declaration statement:",lineobject.is_declaration()

