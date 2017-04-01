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
    pattern = r'\W(?P<type>(' + '|'.join(bd + ed) + '))\*{0,2}\s+.*?(?P<name>\w+)'
    vars_dict = {}
    for function in program_instance.functions:
        vars_dict = {}
        #text_lines = [text_line for text_line in function.text.split('\n') if text_line.strip()]
        for text_line in function.text:
            #print "text line:",text_line
            match = re.search(pattern, text_line)
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
                elif match.group('type') == 'for':
                    ct = match.group('cond').split(';')[1]  # for loop only
                elif match.group('type') == 'while':
                    ct = match.group('cond')  # while and do while
                if re.search(r'[\w ]+=[\w ]+', ct):
                    res.append((line, 0)) #exists
                    continue
            res.append((line, 1))
    return res

def parse_comments(pinst):
    '''
    Takes the programs and it will help in parsing the comments in lines
    '''
    for function in pinst.functions:
        textlines = function.text
        for line in textlines:
            line  = line.strip()
            if '//' in line:
                comment_starts = line.find('//')
            if '/*' in line:
                multiline_comment_starts = line.find('/*')
            
            print line[comment_starts+2:]
            print line[multiline_comment_starts+2:]
            
            if '/*' in line:
                starting_multiline_comment =True
                print line
            
            if starting_multiline_comment is True:
                if line.endswith('*/'):
                    starting_multiline_comment = True
                else:
                    starting_multiline_comment = False
                print line

            if '//' in line and line.endswith('\\'):
                present_backslash = True
            
            if present_backslash is True:
                if line.endswith('\\'):
                    present_backslash = True
                else:
                    present_backslash = False
                print line
