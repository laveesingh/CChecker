
class initialization:

    def __init__(self, text, func='global'):
        self.text = text
        self.function = func

    def process(self, details={}):
        '''
        This would be of the pattern:
        >>> int a, b = 20, c;
        '''
        assign_list = self.text.split(',')
        first_expression = assign_list[0]
        dtype = None
        if re.search(r'\w+\s+\w+', first_expression):
            match = re.search(r'(?P<type>\w+)\s+(?P<name>\w+)', first_expression)
            dtype = match.group('type')
            varname = match.group('name')
            details['variables'][varname]['garbage'] = True
            details['variables'][varname]['datatype'] = dtype
            if '=' in first_expression:
                details['variables'][varname]['garbage'] = False
        elif '=' in first_expression and not re.search(r'\w+\s+\w+', first_expression):
            match = re.search(r'(?P<name>\w+)\s*\=\s*(?P<val>.*)', first_expression)
            varname = match.group('name')
            # dtype must have been defined already
            val_exp = match.group('val')
            details['variables'][varname]['garbage'] = False

        for expression in assign_list[1:]:
            if '=' in expression:
                match = re.search(r'(?P<name>\w+)\s*\=\s*(?P<val>.*)', expression)
                varname = match.group('name')
                details['variables'][varname]['garbage'] = False
                if dtype:
                    details['variables'][varname]['datatype'] = dtype
            else:
                varname = expression.strip()
                details['variables'][varname]['garbage'] = True
                if dtype:
                    details['variables'][varname]['datatype'] = dtype
