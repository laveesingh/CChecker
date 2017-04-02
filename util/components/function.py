
class function:

    properties = {}

    def __init__(self, text, lines):
        self.text = text
        self.start = lines[0]
        self.end = lines[1]
        self.vars = None
        self.comments = {}
        self.assignments_in_cond = []
        self.switch=None
        self.function_name = None
        self.function_calls = []
        self.recursion = 1

    def __eq__(self, other):
        first = self.name == other.name
        second = self.rettype == other.rettype
        third = self.arglist == other.arglist
        return first and second and third
