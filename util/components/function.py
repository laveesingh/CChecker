
class function:

    properties = {}

    def __init__(self, name, rettype, arglist):
        self.name = name
        self.rettype = rettype
        self.arglist = arglist

    def __eq__(self, other):
        first = self.name == other.name
        second = self.rettype == other.rettype
        third = self.arglist == other.arglist
        return first and second and third
