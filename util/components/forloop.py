import sys

# disable creation of *.pyc files
sys.dont_write_bytecode = True


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
