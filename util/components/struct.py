
class struct:

    def __init__(self, text, lines):
        self.text = text
        self.start = lines[0]
        self.end = lines[1]
        self.vars = []
        self.comments = []
        self.assignment_in_cond = []
