
For = [
'for(int i=0; i<n; i++){',
'for(int i=0; i<n; i++) ',
'for(; ; i++)',
'''for
	(int i=0; i<n; i++)'''

]

Blank = [
'',
' ',
'        ',
'\t',
'\r'
]

Dowhile = [
'''do
   {
    body
   }while(condition);'''
]
<<<<<<< HEAD
while=[
'''while(condition)
   {
     body
   }'''
]
switch=[
'''switch(variable)
{
  case value: 
    code
  case value:
    code
  default: 
    code
}'''
]
Declaration=[
 ''' data_type variable_name;
  or 
  data_type variable_name1,variable_name2;'''
]
If=[
'''if ( statement is TRUE )
    Execute this line of code'''
]
Ifelse=[
'''if ( TRUE ) {
     Execute these statements if TRUE 
}
else {
     Execute these statements if FALSE 
}'''
]
Goto=[
'''goto label;
label:
  code
''']
Break=[
'''loop
{
  break;
    code...
}''']
Continue=[
'''for ( int x = 0; x < 10; x++ )
{
  continue;
  cout << x; ' this code is never executed!
}'''
]
Pointerdeclaration=[
'''datatype *variable;'''
]
Function declaration=[
'''type functionName( type [argname] [, type, ...] );'''
]
Function definition=[
'''
type functionName( type argname [, type, ...] )
{
     function body
}''']
Function calling=[
'''function_name( [arg1, ... ] );'''
]
=======

while = [
'while(int i){'
'while(i>0){'
'while(i<n){'
'while( i <= 0){'
'while(int i)'
'while(i>0)'
'while(i<n)'
'while( i <= 0)'
'while( i <= n)'


]
Array declaration=[
'''type name[size];'''
]
Struct=[
'''[typedef] struct [struct_name]
{
    type attribute;
    type attribute2;
    // ...
    [struct struct_name *struct_instance;]
} [struct_name_t] [struct_instance];''']
Pointer_to_a_struct=[
'''struct struct_name *struct_instance;''']

Operators=[
'''
assignment            identifier = value or identifier;
comparision equality  identifier == identifier;
Boolean Or            conditional || conditional;
Boolean And           conditional && conditional;
Boolean Not           !identifier;
Bitwise And           integer_value & integer_value;
Bitwise Or            integer_value | integer_value;
Ternary Operator       <condition> ? <true-case-code>:<false-case-code>;
