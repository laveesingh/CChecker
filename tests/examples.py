
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
Dowhile=[
'''do
   {
    body
   }while(condition);'''
]
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
 ''' 
  data_type variable_name;
  or 
  data_type variable_name1,variable_name2;
  '''
]
If=[
'''
if ( statement is TRUE )
    Execute this line of code
'''
]
Ifelse=[
'''
if ( TRUE ) {
     Execute these statements if TRUE 
}
else {
     Execute these statements if FALSE 
}
'''
]
Goto=[
'''
goto label;

label:
  code
''']
Break=[
'''
loop
{
  break;
    code...
}
''']
Continue=[
'''
for ( int x = 0; x < 10; x++ )
{
  continue;
  cout << x; ' this code is never executed!
}'''
]
Pointerdeclaration=[
'''
datatype *variable;
'''
]
Function declaration=[
'''
type functionName( type [argname] [, type, ...] );'''
]
Function definition=[
'''
type functionName( type argname [, type, ...] )
{
     function body
}''']
