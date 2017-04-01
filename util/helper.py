import re
from store import (
    builtin_datatypes as bd,
    extended_datatypes as ed
)

def parse_vars(program_instance):
    '''
    Takes a program instance and returns a dictionary containing all varibles
    along with their datatypes
    '''
    pattern = r'(?P<type>(' + '|'.join(bd + ed) + ')\s*\*{0,2}\s*)(?P<name>\w+)'
    print "The pattern is ",pattern
    vars_dict = {}
    for function in program_instance.functions:
        text_lines = [text_line for text_line in function.text.split('\n') if text_line.strip()]
        for text_line in text_lines:
            print "text line:",text_line
            match = re.search(pattern, text_line)
            if not match:
                print "Match not found"
                continue
            dtype = match.group('type')
            varname = match.group('name')
            print "First var,dtype",varname,dtype
            vars_dict[varname] = dtype
            csv = text_line.split(',')[1:]
            if csv:
                for declaration in csv:
                    print "declaration",declaration
                    pat = r'(?P<name>\w+).*'
                    match = re.search(pat, declaration)
                    vars_dict[match.group('name')] = dtype
    return vars_dict

condition_st = ('if', 'else if')
loops = ('for', 'while')

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
				elif match.group('type') in loops:
					ct = match.group('cond').split(';')[1]
				if re.search(r'[\w ]*=[\w ]*', ct):
					res.append((line, 0)) #exists
					continue
			res.append((line, 1))
	return res
