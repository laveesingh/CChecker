import re

# def is_switch(self): pass def is_declaration(self): pass def is_assignment(self): pass


class Line:

    def __init__(self, line):
        self.line = line

    ### This function below is idiotic
    def fetch_header_file(self):
        """ Given that it's an include statement """
        header = None
        try:
            header = re.findall('<(.*)>', self.line)[0]
        except IndexError:
            header = re.findall('"(.*)"', self.line)[0]
        except:
            raise Exception("")
        return header[:-2]

    def is_preprocessor(self):
        """
        If the line starts with a '#' it must be a preprocessor
        """
        if self.line.startswith('#'):
            if self.line.startswith('#include'):
                header_file = self.fetch_header_file()
                if header_file not in store['header_files']:
                    raise Exception("Header file is not valid")
            # Other possibilities
            return 1  # it's a preprocessor
        else:
            return 0  # it's not a preprocessor

    def is_preprocessor(self):
        """
        For this line to be a preprocessor, it has to follow the pattern:
        >>> #include something
        >>> #define something
        or some other preprocessor
        """
        self.line = self.line.trim()
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
        self.line = self.line.trim()
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
        self.line = self.line.trim()
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
        self.line = self.line.trim()
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
        self.line = self.line.trim()
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
        self.line = self.line.trim()
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
        self.line = self.line.trim()
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
        self.line = self.line.trim()
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
        self.line = self.line.trim()
        regex = r'switch\s*\(.*\)\s*[\n\{]'
        if re.search(regex, self.line):
            return True
        return False
