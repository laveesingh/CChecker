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
        '''
            For this line to be blank, it should contain, spaces and newline
            characters
        '''
        return not self.line

    def is_comment1(self):
        '''
            Inline comment: // type
            There can be two patterns, either line starts with //
            or line contains comment after some statement/expression.
            But here we're looking, if line starts with comment
        '''
        return self.line.startswith('//')

    def is_comment2(self):
        '''
        Multiline comment: /* ... */ type
        '''
        return self.line.startswith('/*')

    def is_forloop(self):
        '''
            For this line to be a for loop, it has to follow the pattern:
            >>> for(init; condition; increment){
                    body
                }
            Or the pattern:
            >>> for(init; condition; increment)
            {
                body
            }
        '''
        regex = r'for\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False

    def is_whileloop(self):
        '''
            For this line to be while loop, it has to follow the pattern:
            >>> while(condition){
                    body
                }
            Or the pattern:
            >>> while(condition)
                {
                    body
                }
        '''
        regex = r'while\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False

    def is_dowhileloop(self):
        '''
        For this line to be dowhileloop, it has to follow the pattern:
        >>> do{
                body
            } 
        '''
        regex = r'[^\w]do[^\w]'
        if re.search(regex, self.line):
            return True
        return False

    def is_if(self):
        '''
            For this line to be if condition, it has to follow the pattern:
            >>> if(condition){
                    body
                }
            Or the pattern:
            >>> if(condition)
                {
                    body
                }
        '''
        regex = r'if\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False

    def is_elseif(self):
        '''
            For this line to be else if, it has to follow the pattern:
            >>> else if(condition){
                    body
                }
            Or the pattern:
            >>> else if(condition)
                {
                    body
                }
        '''
        regex = r'else if\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False

    def is_else(self):
        '''
            For this line to be else, it has to follow the pattern:
            >>> else(condition){
                    body
                }
            Or the pattern:
            >>> else(condition)
                {
                    body
                }
        '''
        regex = r'else\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False

    def is_switch(self):
        '''
            For this line to be switch, it has to follow the pattern:
            >>> switch(condition){
                    body
                }
            Or the pattern:
            >>> switch(condition)
                {
                    body
                }
        '''
        regex = r'switch\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False

    def is_declaration(self):
        '''
            For this line to be only declaration of variable, it has to follow the
            pattern:
            >>> datatype var_name;
            Or the pattern:
            >>> datatype var1, var2, var3...;
        '''
        regex = r'((const)|(static))?\s*(?P<type>\w+)\s*(?P<name>(\w+)\,?)\s*;'
        if re.search(regex, self.line):
            return True
        return False

    def is_assignment(self):
        '''
        For this line to be assignment, it has to follow the pattern:
        >>> datatype var_name = val;
        sor
        >>> datatype var1 = val1, var2 = val2;
        or
        >>> var_name = val;
        or
        >>> var1 = val1, var2 = val2;
        '''
        regex = r'[^=]\=[^=]'
        if myregex.search(regex, self.line):
            return True
        return False

    def resolve(self):
        '''
        This function will resolve the type of the given line.
        '''
        inst = statement(self.line, self.number)
        if inst.is_blank(): return 'blank'
        if inst.is_comment1(): return 'comment1'
        if inst.is_preprocessor(): return 'preprocessor'
        if inst.is_function_prototype(): return 'function_prototype'
        if inst.is_function_definition(): return 'function_definition'
        if inst.is_forloop(): return 'forloop'
        if inst.is_whileloop(): return 'whileloop'
        if inst.is_dowhileloop(): return 'dowhileloop'
        if inst.is_if(): return 'ifcondition'
        if inst.is_elseif(): return 'elseifcondition'
        if inst.is_else(): return 'elsecondition'
        if inst.is_swith(): return 'switch'
        if inst.is_declaration(): return 'declaration'
        if inst.is_assigment(): return 'assignment'
        if inst.is_struct(): return 'struct'
        return 'screwed'
