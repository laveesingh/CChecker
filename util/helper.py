import re
from store import (
    builtin_datatypes as bd
)

def parse_vars(program_instance):
    '''
    Takes a program instance and returns a dictionary containing all varibles
    along with their datatypes
    '''
    modifiers = r'(const|auto|static|register|extern|volatile|signed|unsigned )*'
    fpattern = r'\W' + modifiers + '(?P<type>'
    spattern = ')\*{0,2}\s+.*?' + modifiers + '(?P<name>\w+)[^\(\)]*$'
    for function in program_instance.functions:
        vars_dict = {}
        #text_lines = [text_line for text_line in function.text.split('\n') if text_line.strip()]
        for text_line in function.text:
            #print "text line:",text_line
            match = None
            for pos_dtype in bd:
                pattern = fpattern + pos_dtype + spattern
                match = re.search(pattern, text_line)
                if match:
                    break
            if not match:
                #print "Match not found"
                continue
            dtype = match.group('type')
            varname = match.group('name')
            #print "First var,dtype",varname,dtype
            vars_dict[varname] = dtype
            csv = text_line.split(',')[1:]
            if csv:
                for declaration in csv:
                    pat = r'(?P<name>\w+).*'
                    match = re.search(pat, declaration)
                    vars_dict[match.group('name')] = dtype
        function.vars = vars_dict

condition_st = ('if', 'else if', 'while')
loops = ('for')

def conditions(pinst):
    ''''''
    res = []
    for func in pinst.functions:
        textlines = func.text
        for line in textlines:
            line = line.strip()
            #res.append(line)
            match = re.search(r'(?P<type>\w*)\((?P<cond>.*)\)', line)
            if not match:
                continue
            if match.group('type') in condition_st or match.group('type') in loops:
                if match.group('type') in condition_st:
                    ct = match.group('cond')
                elif match.group('type') == 'for':
                    ct = match.group('cond').split(';')[1]  # for loop only
                if re.search(r'[\w ]+=[\w ]+', ct):
                    func.assignments_in_cond.append(line) #exists
                    continue
            res.append((line, 1))
    return res

def parse_comments(pinst):
    '''
    Takes the programs and it will help in parsing the comments in lines
    '''
    
    for function in pinst.functions:
        i=0
        text_lines = function.text
        while i < len(text_lines):
            #i = i + 1
            #print str(i),':',line
            line = text_lines[i]
            if '//' in line:
                starts = i
                while line.endswith('\\\n'):
                    i = i + 1
                    line = text_lines[i]
                function.comments.append(text_lines[starts:i+1])
            if '/*' in line:
                starts = i
                #print 'Hey'
                while '*/' not in line:
                    i = i + 1 
                    line = text_lines[i]
                function.comments.append(text_lines[starts:i+1])
            i = i + 1

def find_goto(program):
    for function in pinst.functions:
        textlines = function.text
        pattern = r'(\W+)|(\b)(goto|continue)(\W+)|(\b)'
        for line in textlines:
            if re.search(pattern, line):
                print line

def find_dynamic_memory_allocation(program):
    for function in pinst.functions:
        textlines = function.text
        pattern = r'(\W+)|(\b)(malloc|calloc|realloc|free)(\W+)|(\b)'
        for line in textlines:
            if re.search(pattern, line):
                print line

def comparison_floating(pinst):
    ''''''
    comp_op = ["==", "<=", ">=", "!=", "<", ">"]
    for func in pinst.functions:
        if func.vars is None:
            parse_vars(pinst)
        for line in func.text:
            if any(cmp in line for cmp in comp_op):
                line = line.strip()
                match = re.search(r'(?P<type>\w*)\((?P<cond>.*)\)', line)
                if not match:
                    continue
                #print line
                if match.group('type') in condition_st:
                    res = re.search(r"(\w*\(\s*(?P<a>[\w\*\\+-]*)\s*((>=)|(>)|(<)|(<=)|(==)|(!=))\s*(?P<b>[\w\*\\+-]*)\s*\).*)", line)
                    if res:
                        pass
                        #print res.group('a'), res.group('b')
                elif match.group('type') in loops:
                    cond = match.group('cond').split(';')[1]
                    res = re.search(r"(\s*(?P<a>[\w\*\\+-]*)\s*((>=)|(>)|(<)|(<=)|(==)|(!=))\s*(?P<b>[\w\*\\+-]*)\s*)", cond)
                    if res:
                        pass
                        #print res.group('a'), res.group('b')
                


