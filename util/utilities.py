import re
import sys

import myregex
import store

before_pattern = r'(?P<before>.*?)'
after_pattern = r'(?P<after>.*?)'

# disable creation of *.pyc files
sys.dont_write_bytecode = True


class statement:

    def __init__(self, line, number):
        self.line = line.strip()
        self.number = number  # line number in program

    def is_blank(self):
        """
            For this line to be blank, it should contain, spaces and newline
            characters
        """
        return not self.line

    def is_comment1(self):
        """
            Inline comment: // type
            There can be two patterns, either line starts with //
            or line contains comment after some statement/expression.
            But here we're looking, if line starts with comment
        """
        return self.line.startswith('//')

    def is_preprocessor(self):
        """
            For this line to be a preprocessor, it has to follow the pattern:
            >>> #include something
            >>> #define something
            or some other preprocessor
        """
        regex = r'\#((include)|(define)).*'
        if re.search(regex, self.line):
            return True
        return False

    def is_function_prototype(self):
        """
            For this line to be a function prototype, it has to follow the pattern:
            >>> return_type function_name(type1 arg1...);
            1. It starts at a return type, built in or self defined. This is
            followed by one or more spaces.
            2. Then comes the function name followed by parantheses
            3. There may be zero of more space characters between function name and
            the parantheses.
            4. Parantheses contain argument list, closing parantheses is followed
            by a semicolon;
        """
        regex = r'((?P<ret>[a-zA-Z_]\w*)\*?\s+\*?(?P<name>[a-zA-Z_]\w*)\s*' +\
            r'\(.*\)\s*\;)'
        if re.search(regex, self.line):
            return True
        return False

    def is_function_definition(self):
        """
            For this line to be a function definition, it has to follow the
            pattern:
            >>> return_type function_name(type1 arg1...) {
                    definition
                }
            Or the pattern:
            >>> return_type function_name(type1 arg1...)
            {
                    definition
            }
            1. It starts at a return type, built in or self defined. This is
            followed by one or more spaces.
            2. Then comes the function name followed by parantheses
            3. There may be zero of more space characters between function name and
            the parantheses.
            4. Parantheses contain argument list, closing parantheses is followed
            by a { or newline;
        """
        regex = r'((?P<ret>[a-zA-Z_]\w*)\*?\s+\*?(?P<name>[a-zA-Z_]\w*)\s*' +\
            r'\(.*\)\s*\[\n\{])'
        if re.search(regex, self.line):
            return True
        return False

    def is_forloop(self):
        """
            For this line to be a for loop, it has to follow the pattern:
            >>> for(init; condition; increment){
                    body
                }
            Or the pattern:
            >>> for(init; condition; increment)
            {
                body
            }
        """
        regex = r'for\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False

    def is_whileloop(self):
        """
            For this line to be while loop, it has to follow the pattern:
            >>> while(condition){
                    body
                }
            Or the pattern:
            >>> while(condition)
                {
                    body
                }
        """
        regex = r'while\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False

    def is_if(self):
        """
            For this line to be if condition, it has to follow the pattern:
            >>> if(condition){
                    body
                }
            Or the pattern:
            >>> if(condition)
                {
                    body
                }
        """
        regex = r'if\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False

    def is_elseif(self):
        """
            For this line to be else if, it has to follow the pattern:
            >>> else if(condition){
                    body
                }
            Or the pattern:
            >>> else if(condition)
                {
                    body
                }
        """
        regex = r'else if\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False

    def is_else(self):
        """
            For this line to be else, it has to follow the pattern:
            >>> else(condition){
                    body
                }
            Or the pattern:
            >>> else(condition)
                {
                    body
                }
        """
        regex = r'else\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False

    def is_switch(self):
        """
            For this line to be switch, it has to follow the pattern:
            >>> switch(condition){
                    body
                }
            Or the pattern:
            >>> switch(condition)
                {
                    body
                }
        """
        regex = r'switch\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False

    def is_declaration(self):
        """
            For this line to be only declaration of variable, it has to follow the
            pattern:
            >>> datatype var_name;
            Or the pattern:
            >>> datatype var1, var2, var3...;
        """
        regex = r'((const)|(static))?\s*(?P<type>\w+)\s*(?P<name>(\w+)\,?)\s*;'
        if re.search(regex, self.line):
            return True
        return False

    def is_assignment(self):
        """
        For this line to be assignment, it has to follow the pattern:
        >>> datatype var_name = val;
        or
        >>> datatype var1 = val1, var2 = val2;
        or
        >>> var_name = val;
        or
        >>> var1 = val1, var2 = val2;
        """
        regex = r'[^=]\=[^=]'
        if myregex.search(regex, self.line):
            return True
        return False

    def is_struct(self):
        """
        For this line to be struct, it has to follow the pattern:
        >>> struct name{
                body
            };
        >>> typedef struct name{
                body
            };
        """
    





class function:

    properties = {}

    def __init__(self, index, text, start, end):
        self.index = index
        self.text = text
        self.start = start
        self.end = end

    def process(self, details={}):
        lines_list = self.text.split('\n')
        mid_pattern = r'(?P<ret>\w+\*{0,2})\s+(?P<name>\w+)\s*\((?P<args>.*?)\)'  # not handled case where pointer(*) is with function name
        first_line_pattern = before_pattern + mid_pattern + after_pattern
        match = re.search(first_line_pattern, lines_list[0].strip())
        self.name = match.group('name')
        self.rettype = match.group('ret')
        args = match.group('args')

class forloop:

    def __init__(self, index, level, text, start, end):
        self.index = index
        self.level = level
        self.text = text
        self.start = start
        self.end = end

    def process(self, details={}):
        lines_list = self.text.split('\n')
        mid_pattern = r'for\s*\((?P<init>.*?);\s*(?P<cond>.*?);\s*(?P<inc>.*?)\)\n'
        first_line_pattern = before_pattern + mid_pattern + after_pattern
        match = re.search(first_line_pattern, lines_list[0].strip())
        init = match.group('init')
        cond = match.group('cond')
        inc = match.group('inc')
        before = match.group('before')
        after = match.group('after')
        # todo: process init, according to assignment processor and 
        # fill deails

class whileloop:

    def __init__(self, index, level, text, start, end):
        self.index = index
        self.level = level
        self.text = text
        self.start = start
        self.end = end

    def process(self, details={}):
        lines_list = self.text.split('\n')
        mid_pattern = r'while\s*\((?P<cond>.*?)\)(?P<after>.*)\n'
        first_line_pattern = before_pattern + mid_pattern + after_pattern
        match = re.search(first_line_pattern, lines_list[0].strip())
        before = match.group('before')
        after = match.group('after')
        cond = match.group('cond')
        # there's nothing much to do in this initial stage here

class dowhileloop:

    def __init__(self, index, level, text, start, end):
        self.index = index
        self.level = level
        self.text = text
        self.start = start
        self.end = end

    def process(self, details={}):
        lines_list = self.text.split('\n')
        last_mid_pattern = r'while\s*\((?P<cond>.*?)\)'
        last_line_pattern = before_pattern + last_mid_pattern + after_pattern
        match = re.search(last_line_pattern, lines_list[-1].strip())
        before = match.group('before')
        after = match.group('after')
        cond = match.group('cond')
        # there's nothing much to do in this initial stage here


class ifcondition:

    def __init__(self, index, level, text, start, end):
        self.index = index
        self.level = level
        self.text = text
        self.start = start
        self.end = end


class elseifcondition:

    def __init__(self, index, level, text):
        self.index = index
        self.level = level
        self.text = text

    def ex():
        pass

class switch:

    def __init__(self, index, level, text):
        self.index = index
        self.level = level
        self.text = text

    def ex():
        pass

class struct:

    def __init__(self, index, level, text):
        self.index = index
        self.level = level
        self.text = text

    def ex():
        pass


class elsecondition:

    def __init__(self, index, level, text):
        self.index = index
        self.level = level
        self.text = text

    def ex():
        pass


class initialization:

    def __init__(self, text, func='global'):
        self.text = text
        self.function = func

    def process(self, details={}):
        """
        This would be of the pattern:
        >>> int a, b = 20, c;
        """
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
