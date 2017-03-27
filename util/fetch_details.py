'''
This file is actually to help process any kind of statement and fetch all kinds
of runtime details into a given dictionary
'''
import re


def initialization(text, details={}):
    '''
    text given is a statement that contains declaration, initialization of
    variables, this function processes the statement and puts the details about
    such variables into details dictionary
    '''
    assign_list = text.split(',')
    first_expression = assign_list[0]
    dtype = None
    if re.search(r'\w+\s+\w+', first_expression):
        match = re.search(r'(?P<type>\w+)\s+(?P<name>\w+)\s*[\=$]', first_expression)
        dtype = match.group('type')
        varname = match.group('name')
        if details.get(varname) is None:
            details[varname] = {}
        details[varname]['garbage'] = True
        details[varname]['datatype'] = dtype
        if '=' in first_expression:
            details[varname]['garbage'] = False
    elif '=' in first_expression and not re.search(r'\w+\s+\w+', first_expression):
        match = re.search(r'(?P<name>\w+)\s*\=\s*(?P<val>.*)', first_expression)
        varname = match.group('name')
        # dtype must have been defined already
        val_exp = match.group('val')
        details[varname]['garbage'] = False

    for expression in assign_list[1:]:
        if '=' in expression:
            match = re.search(r'(?P<name>\w+)\s*\=\s*(?P<val>.*)', expression)
            varname = match.group('name')
            details[varname]['garbage'] = False
            if dtype:
                details['variables'][varname]['datatype'] = dtype
        else:
            varname = expression.strip()
            details['variables'][varname]['garbage'] = True
            if dtype:
                details['variables'][varname]['datatype'] = dtype
