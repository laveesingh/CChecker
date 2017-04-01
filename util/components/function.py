
class function:

    properties = {}

    def __init__(self, text, lines):
        self.text = text
        self.start = lines[0]
        self.end = lines[1]

    def __eq__(self, other):
        first = self.name == other.name
        second = self.rettype == other.rettype
        third = self.arglist == other.arglist
        return first and second and third
