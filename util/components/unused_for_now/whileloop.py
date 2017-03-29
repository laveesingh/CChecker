
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
