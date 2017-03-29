import sys

# disable creation of *.pyc files
sys.dont_write_bytecode = True


before_pattern = 
after_pattern = 

class forloop:

    def __init__(self, lines_list, start, end, env={}):
        self.lines_list = lines_list
        self.start = start
        self.end = end
        self.env = env  #environment details

    def process(self, details={}):
        first_line_pattern = r'(?P<before>.*?)' + r'for\s*\((?P<init>.*?);\s*(?P<cond>.*?);\s*(?P<inc>.*?)\)' + r'(?P<after>.*?)'
        match = re.search(first_line_pattern, lines_list[0].strip())
        init = match.group('init')
        cond = match.group('cond')
        inc = match.group('inc')
        before = match.group('before')
        after = match.group('after')
        # todo: process init, according to assignment processor and 
        # fill deails
