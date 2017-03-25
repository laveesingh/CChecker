import re
import myregex

from store import store


class statement:

    def __init__(self, line, number):
        self.line = line
        self.number = number  # line number in program

    def is_blank(self):
        """
            For this line to be blank, it should contain, spaces and newline
            characters
        """
        self.line = self.line.strip()
        return not self.line

    def is_comment1(self):
        """
            Inline comment: // type
            There can be two patterns, either line starts with //
            or line contains comment after some statement/expression.
            But here we're looking, if line starts with comment
        """
        self.line = self.line.strip()
        return self.line.startswith('//')

    def is_preprocessor(self):
        """
            For this line to be a preprocessor, it has to follow the pattern:
            >>> #include something
            >>> #define something
            or some other preprocessor
        """
        self.line = self.line.strip()
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
        self.line = self.line.strip()
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
        self.line = self.line.strip()
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
        self.line = self.line.strip()
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
        self.line = self.line.strip()
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
        self.line = self.line.strip()
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
        self.line = self.line.strip()
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
        self.line = self.line.strip()
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
        self.line = self.line.strip()
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
        self.line = self.line.strip()
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
        self.line = self.line.strip()
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

    def __init__(self, name, startmark, text, rettype='int', arglist=[]):
        """
        name: Name of the function
        startmark: Line number where the function definition starts
        rettype: return data type
        arglist: parameter list that it takes
        """
        self.name = name
        self.startmark = startmark
        self.text = text
        self.rettype = rettype
        seslf.arglist = arglist

    def __eq__(self, other):
        return self.name == other.name and self.rettype == other.rettype and
            self.arglist == other.arglist


class forloop:

    def __init__(self, index, level, text):
        self.index = index
        self.level = level
        self.text = text

    def ex():
        pass


class whileloop:

    def __init__(self, index, level, text):
        self.index = index
        self.level = level
        self.text = text

    def ex():
        pass


class dowhileloop:

    def __init__(self, index, level, text):
        self.index = index
        self.level = level
        self.text = text

    def ex():
        pass


class ifcondition:

    def __init__(self, index, level, text):
        self.index = index
        self.level = level
        self.text = text

    def ex():
        pass


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


def variable:

    def __init__(self, 
