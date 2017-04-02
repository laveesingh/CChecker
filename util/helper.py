import re
from store import (
    builtin_datatypes as bd
)
from collections import defaultdict


def is_assignment(line):
    '''
    checkes if given line is assignment of some kind
    '''
    pat = r'[\w ]=[\w ]'
    return bool(re.search(pat, line))


def parse_vars(program_instance):
    '''
    Takes a program instance and returns a dictionary containing all varibles
    within all functions
    along with their datatypes
    '''
    modifiers = r'(?P<mod>(const|auto|static|register|extern|volatile|signed|unsigned| )*)'
    fpattern = r'' + modifiers + r'\s*(?P<type>'
    spattern = r')\*{0,2}.*?(?P<name>\w+)[^\(]*$'
    for function in program_instance.functions:
        vars_dict = {}
        #text_lines = [text_line for text_line in function.text.split('\n') if text_line.strip()]
        for text_line in function.text:
            #print "text line:",text_line,
            match = None
            for pos_dtype in bd:
                pattern = fpattern + pos_dtype + spattern
                #print "pattern:",pattern
                match = re.search(pattern, text_line)
                if match:
                    #print "match"
                    break
            if not match:
                #print "Match not found"
                continue
            dtype = match.group('type')
            varname = match.group('name')
            #print "First var,dtype",varname,dtype
            unsigned = 0
            if match.group('mod') is not None and 'unsigned' in match.group('mod'):
                unsigned = 1
            vars_dict[varname] = (dtype, unsigned) # unsigned is 1 if dtype is unsigned, 0 otherwise
            csv = text_line.split(',')[1:]
            if csv:
                for declaration in csv:
                    pat = r'(?P<name>\w+).*'
                    match = re.search(pat, declaration)
                    vars_dict[match.group('name')] = (dtype, unsigned)
        function.vars = vars_dict

def parse_struct_vars(program_instance):
    '''
    Takes a program instance and returns a dictionary containing all varibles
    within all structures along with their datatypes
    '''
    modifiers = r'(?P<mod>(const|auto|static|register|extern|volatile|signed|unsigned| )*)'
    fpattern = r'' + modifiers + '\s+(?P<type>'
    spattern = ')\*{0,2}\s+.*?(?P<name>\w+)'
    for struct in program_instance.structs:
        vars_dict = {}
        for text_line in struct.text:
            match = None
            for pos_dtype in bd:
                pattern = fpattern + pos_dtype + spattern
                match = re.search(pattern, text_line)
                if match:
                    break
            if not match:
                continue
            dtype = match.group('type')
            varname = match.group('name')
            unsigned = 0
            if match.group('mod') is not None and 'unsigned' in match.group('mod'):
                unsigned = 1
            vars_dict[varname] = (dtype, unsigned) # unsigned is 1 if dtype is unsigned, 0 otherwise
            csv = text_line.split(',')[1:]
            if csv:
                for declaration in csv:
                    pat = r'(?P<name>\w+).*'
                    match = re.search(pat, declaration)
                    vars_dict[match.group('name')] = (dtype, unsigned)
        struct.vars = vars_dict


def parse_union_vars(program_instance):
    '''
    Takes a program instance and returns a dictionary containing all varibles
    within all structures along with their datatypes
    '''
    modifiers = r'(?P<mod>(const|auto|static|register|extern|volatile|signed|unsigned| )*)'
    fpattern = r'' + modifiers + '\s+(?P<type>'
    spattern = ')\*{0,2}\s+.*?(?P<name>\w+)'
    for union in program_instance.unions:
        vars_dict = {}
        for text_line in union.text:
            match = None
            for pos_dtype in bd:
                pattern = fpattern + pos_dtype + spattern
                match = re.search(pattern, text_line)
                if match:
                    break
            if not match:
                continue
            dtype = match.group('type')
            varname = match.group('name')
            unsigned = 0
            if match.group('mod') is not None and 'unsigned' in match.group('mod'):
                unsigned = 1
            vars_dict[varname] = (dtype, unsigned) # unsigned is 1 if dtype is unsigned, 0 otherwise
            csv = text_line.split(',')[1:]
            if csv:
                for declaration in csv:
                    pat = r'(?P<name>\w+).*'
                    match = re.search(pat, declaration)
                    vars_dict[match.group('name')] = (dtype, unsigned)
        union.vars = vars_dict

def parse_global_vars(program_instance):
    '''
    Takes a program instance and returns a dictionary containing all varibles
    within all structures along with their datatypes
    '''
    modifiers = r'(?P<mod>(const|auto|static|register|extern|volatile|signed|unsigned| )*)'
    fpattern = r'' + modifiers + '\s+(?P<type>'
    spattern = ')\*{0,2}\s+.*?(?P<name>\w+)'
    vars_dict = {}
    for gv in program_instance.global_vars:
        statement = gv.text[0]
        match = None
        for pos_dtype in bd:
            pattern = fpattern + pos_dtype + spattern
            match = re.search(pattern, statement)
            if match:
                break
        if not match:
            continue
        dtype = match.group('type')
        varname = match.group('name')
        unsigned = 0
        if match.group('mod') is not None and 'unsigned' in match.group('mod'):
            unsigned = 1
        vars_dict[varname] = (dtype, unsigned)
        csv = statement.split(',')[1:]
        if csv:
            for declaration in csv:
                pat = r'(?P<name>\w+).*'
                match = re.search(pat, declaration)
                vars_dict[match.group('name')] = (dtype, unsigned)

    program_instance.global_vars_dict = vars_dict


condition_st = ('if', 'else if', 'while')
loops = ('for')

def conditions(pinst):
    ''''''
    res = []
    for func in pinst.functions:
        textlines = func.text
        st = func.start - 1
        for line in textlines:
            st += 1
            line = line.strip()
            #res.append(line)
            #match = re.search(r'(?P<type>\w*)\s*\(\s*(?P<cond>[\w\*\\+-=]*)\s*\).*', line)
            match = re.search(r'(?P<type>\w*)\s*\((?P<cond>.*?)\)', line)
            if not match:
                continue
            if match.group('type') in condition_st or match.group('type') in loops:
                ct = None
                if match.group('type') in condition_st:
                    ct = match.group('cond')
                elif match.group('type') == 'for':
                    ct = match.group('cond').split(';')[1]  # for loop only
                if ct and re.search(r'[\w ]+=[\w ]+', ct):
                    res.append(st+1) #exists
    return res

def parse_comments(pinst):
    '''
    Takes the programs and it will help in parsing the comments in lines
    '''

    for function in pinst.functions:
        orstart = function.start
        text_lines = function.text
        i = 0
        while i < len(text_lines):
            #i = i + 1
            #print str(i),':',line
            line = text_lines[i]
            if '//' in line:
                starts = i
                while line.endswith('\\\n'):
                    i = i + 1
                    line = text_lines[i]
                function.comments[function.start + starts] = text_lines[starts:i+1]
            if '/*' in line:
                starts = i
                #print 'Hey'
                while '*/' not in line:
                    i = i + 1
                    line = text_lines[i]
                function.comments[function.start + starts] = text_lines[starts:i+1]
            i = i + 1

def find_goto(pinst):
    ''''''
    goto_list = []
    for function in pinst.functions:
        textlines = function.text
        st = function.start - 1
        pattern = r'(\W*)(goto|continue)(\b)(' ')?'
        for line in textlines:
            st += 1
            if re.search(pattern, line):
                goto_list.append(st + 1)
    return goto_list

def find_dynamic_memory_allocation(pinst):
    ''''''
    dynamic_list = []
    for function in pinst.functions:
        textlines = function.text
        st = function.start - 1
        pattern = r'(\W*)(malloc|calloc|realloc|free)(\b)(' ')?'
        for line in textlines:
            st += 1
            line = line.strip('\n')
            if re.search(pattern, line):
                dynamic_list.append(st+1)
    return dynamic_list

def comparison_floating(pinst):
    ''''''
    comp_op = ["==", "<=", ">=", "!=", "<", ">"]
    result = []
    for func in pinst.functions:
        if func.vars is None:
            parse_vars(pinst)
        lineno = func.start -1
        for line in func.text:
            lineno += 1
            if any(cmp in line for cmp in comp_op):
                line = line.strip()
                match = re.search(r'(?P<type>\w+)\s*\(\s*(?P<cond>.+)\s*\).*', line)
                if not match:
                    continue
                #print line
                if match.group('type') in condition_st:
                    res = re.search(r"(\w*\(\s*(?P<a>[\w\*\(\)\+-/]+)\s*((>=)|(>)|(<)|(<=)|(==)|(!=))\s*(?P<b>[\w\*\(\)\+-/]+)\s*\).*)", line)
                    if res:
                        ares = (res.group('a').strip('(')).strip(')')
                        bres = (res.group('b').strip('(')).strip(')')
                        ares, bres = handle_eq(ares, bres)
                        at = which_type(ares)
                        bt = which_type(bres)
                        if at is 3:
                            #print "Shit Happens!" + ares
                            pass
                        elif at is 0:
                            #print func.vars, ares
                            at = func.vars.get(ares)
                            if at is None:
                                #print "Sucks!" + ares
                                pass
                            else:
                                at = at[0]
                        if bt is 3:
                            #print "Shit Happens!" + bres
                            pass
                        elif bt is 0:
                            #print func.vars, bres
                            bt = func.vars.get(bres)
                            if bt is None:
                                #print "Sucks!" + bres
                                pass
                            else:
                                bt = bt[0]
                        if at in ['float', 'double'] and bt in ['float', 'double']:
                            result.append(lineno+1)
                        #print res.group('a'), res.group('b')
                elif match.group('type') in loops:
                    #print match.group('type')
                    cond = match.group('cond').split(';')[1]
                    res = re.search(r"(\s*(?P<a>[\w\*\(\)+-/]+)\s*((>=)|(>)|(<)|(<=)|(==)|(!=))\s*(?P<b>[\w\*\(\)\+-/]*)\s+)", cond)
                    if res:
                        ares = (res.group('a').strip('(')).strip(')')
                        bres = (res.group('b').strip('(')).strip(')')
                        ares, bres = handle_eq(ares, bres)
                        at = which_type(ares)
                        bt = which_type(bres)
                        if at is 3:
                            #print "Shit Happens!" + ares
                            pass
                        elif at is 0:
                            #print func.vars, ares
                            at = func.vars.get(ares)
                            if at is None:
                                #print "Sucks!" + ares
                                pass
                            else:
                                at = at[0]
                        if bt is 3:
                            #print "Shit Happens!" + bres
                            pass
                        elif bt is 0:
                            #print func.vars, bres
                            bt = func.vars.get(bres)
                            if bt is None:
                                #print "Sucks!" + bres
                                pass
                            else:
                                bt = bt[0]
                        if at in ['float', 'double'] and bt in ['float', 'double']:
                            result.append(lineno+1)
                        #print res.group('a'), res.group('b')
    return result

def which_type(val):
    ''''''
    if '.' in val:
        return 'float'
    try:
        int(val)
        return 'int'
    except ValueError:
        return 0
    return 3

def handle_eq(x, y):
    ''''''
    matched = re.search(r'((?P<x>\w*)\s*((\+)|(-)|(\*)|(/))\s*(?P<y>\w*))', x)
    if matched:
        try:
            int(matched.group('x'))
            x = matched.group('y')
        except ValueError:
            x = matched.group('x')
    matched = re.search(r'((?P<x>\w*)\s*((\+)|(-)|(\*)|(/))\s*(?P<y>\w*))', y)
    if matched:
        try:
            int(matched.group('x'))
            y = matched.group('y')
        except ValueError:
            y = matched.group('x')
    return x, y

def single_comments(pinst):
    ''''''
    res = []
    for comm in pinst.global_comments:
        text = comm.text[0].strip()
        lno = comm.start
        if text.startswith('//'):
            res.append(lno + 1)

    parse_comments(pinst)

    for fun in pinst.functions:
        #print fun.comments
        for lno in fun.comments:
            #print comm, lno
            text = fun.comments[lno][0].strip()
            #print lno, text
            if text.startswith('//'):
                res.append(lno + 1)

    return res

def is_switch(line):
    res = re.search(r'(;)?switch(.*).*',line)
    if res :
        return True
    return False

def parse_switch(pinst):
    result = []
    for func in pinst.functions:
        line_text=func.text
        ostart = func.start
        index=0
        while index < len(line_text):
            if is_switch(line_text[index]):
                starts=index
                no_of_cbraces = 0
                if '{' in line_text[index]:
                    no_of_cbraces = 1
                index += 1
                while True:
                    no_of_cbraces += line_text[index].count('{')
                    no_of_cbraces -= line_text[index].count('}')
                    if no_of_cbraces == 0 or index == len(line_text) - 1:
                        ends = index
                        break
                    index += 1
                text=''.join(line_text[starts:index+1])
                #match = re.search(r'\((?P<cond>.*)\)', text)
                if 'default' not in text:
                    result.append(ostart + starts + 1)
                #func.switch=(match.group('cond'),state)
                #print func.switch
                #print 'Text Switch : ',line_text[starts:ends+1]
            else:
                index += 1
                pass
    return result

def if_else(pinst):
    result = []
    if_pattern = r'(\W*)(if)(\b)(\W*)'
    else_if_pattern = r'(\W*)(else if)(\b)(\W*)'
    else_pattern = r'(\W*)(else)(\b)(\W*)'
    i = 0
    previous_ifs = None
    for function in pinst.functions:
        lineno = function.start - 1
        for line in function.text:
            lineno += 1
            if re.search(else_if_pattern, line):
                continue
            if re.search(if_pattern, line):
                if i > 1:
                    result.append(previous_ifs + 1)
                    i = 0
                previous_ifs = lineno
                i += 1
            if re.search(else_pattern, line):
                i -= 1
    if i > 0:
        result.append(previous_ifs + 1)
    return result 

def is_float(dtype):
    if 'float' in dtype or 'double' in dtype:
        return True
    return False

def check_implicit_type_conversion(pinst):
    '''
    Explicit type conversion is human,
    implicit type conversion is divine.
    '''
    result = []
    lines_list = []
    pat = r'(?P<var1>\w+)\s*=\s*(\((?P<tcast>\w+)\))?.*?(?P<var2>\w+)' #this pattern can be malicious, adding \s* at the end may redefine
    for function in pinst.functions:
        lines_list = function.text
        lineno = function.start - 1
        for line in lines_list:
            lineno += 1
            if is_assignment(line):
                statements = line.split(',')
                for statement in statements:
                    if is_assignment(statement):
                        match = re.search(pat, statement)
                        if not function.vars:
                            parse_vars(pinst)
                        if function.vars.get(match.group('var1')) is None or function.vars.get(match.group('var2')) is None:  # This variable isn't set
                            continue
                        type1, signed1 = function.vars[match.group('var1')]
                        type2, signed2 = function.vars[match.group('var2')]
                        if match.group('tcast'):
                            # Type cast is explicit
                            continue
                        if is_float(type1) != is_float(type2) or signed1 != signed2:
                            result.append(lineno + 1)
                            #print "implicite type conversion violated.  line:", statement
    for struct in pinst.structs:
        lines_list = struct.text
        lineno = struct.start - 1
        for line in lines_list:
            lineno += 1
            if is_assignment(line):
                statements = line.split(',')
                for statement in statements:
                    if is_assignment(statement):
                        match = re.search(pat, statement)
                        if not struct.vars:
                            parse_struct_vars(pinst)
                        if struct.vars.get(match.group('var1')) is None or struct.vars.get(match.group('var2')) is None:  # This variable isn't set
                            continue
                        type1 = struct.vars[match.group('var1')]
                        type2 = struct.vars[match.group('var2')]
                        if match.group('tcast'):
                            # Type cast is explicit
                            continue
                        if is_float(type1) or is_float(type2):
                            result.append(lineno + 1)
                            #print "implicite type conversion violated.  line:", statement
    for union in pinst.unions:
        lines_list = union.text
        lineno = union.start - 1
        for line in lines_list:
            lineno += 1
            if is_assignment(line):
                statements = line.split(',')
                for statement in statements:
                    if is_assignment(statement):
                        match = re.search(pat, statement)
                        if not union.vars:
                            parse_union_vars(pinst)
                        if union.vars.get(match.group('var1')) is None or union.vars.get(match.group('var2')) is None:  # This variable isn't set
                            continue
                        type1 = union.vars[match.group('var1')]
                        type2 = union.vars[match.group('var2')]
                        if match.group('tcast'):
                            # Type cast is explicit
                            continue
                        if is_float(type1) or is_float(type2):
                            result.append(lineno + 1)
                            #print "implicite type conversion violated.  line:", statement
    # Global vars remaining are remaining
    for gvar in pinst.global_vars:
        line = gvar.text[0]
        #print line
        lineno = gvar.start
        if is_assignment(line):
            statements = line.split(',')
            for statement in statements:
                if is_assignment(statement):
                    match = re.search(pat, statement)
                    if not match:
                        print "PAT:", pat, 'STATEMENT:', statement
                        print "regex matching screwed up"
                        continue
                    if not pinst.global_vars_dict:
                        parse_global_vars(pinst)
                    if pinst.global_vars_dict.get(match.group('var1')) is None or pinst.global_vars_dict.get(match.group('var2')) is None:
                        # Either of these variables isn't set in base
                        continue
                    type1 = pinst.global_vars_dict[match.group('var1')]
                    type2 = pinst.global_vars_dict[match.group('var2')]
                    if match.group('tcast'):
                        # Type cast is explicit
                        continue
                    if is_float(type1) or is_float(type2):
                        result.append(lineno + 1)
                        #print "implicite type conversion violated.  line:", statement
    return result

def check_initialized_variable(pinst):
    result = []
    pat = r'.*(?P<var1>\w+)\W*= (?P<rhs>.*)'  #This pattern may malfunction
    for function in pinst.functions:
        initialized = {}
        st = function.start -1
        for gvar in pinst.global_vars_dict:
            initialized[gvar] = True
        for line in function.text:
            st += 1
            if is_assignment(line):
                statements = line.split(',')
                for statement in statements:
                    if is_assignment(statement):
                        print "PAT:",pat,"STATEMENT:",statement
                        match = re.search(pat, statement)
                        if not match:
                            continue
                        varname = match.group('var1')
                        initialized[varname] = True
                        rhs = match.group('rhs')
                        words = re.findall(r'\w+', rhs)
                        for word in words:
                            if word in function.vars and not initialized.get(word):
                                result.append(st + 1)
                                #print "Suspicious initialization statement:",statement
    for struct in pinst.structs:
        initialized = {}
        st = struct.start - 1
        for line in struct.text:
            st += 1
            if is_assignment(line):
                statements = line.split(',')
                for statement in statements:
                    if is_assignment(statement):
                        match = re.search(pat, statement)
                        varname = match.group('var1')
                        initialized[varname] = True
                        rhs = match.group('rhs')
                        words = re.findall(r'\w+', rhs)
                        for word in words:
                            if word in struct.vars and not initialized.get(word):
                                result.append(st + 1)
                                #print "Suspicious initialization statement:",statement
    for union in pinst.unions:
        initialized = {}
        st = union.start - 1
        for line in union.text:
            st += 1
            if is_assignment(line):
                statements = line.split(',')
                for statement in statements:
                    if is_assignment(statement):
                        match = re.search(pat, statement)
                        varname = match.group('var1')
                        initialized[varname] = True
                        rhs = match.group('rhs')
                        words = re.findall(r'\w+', rhs)
                        for word in words:
                            if word in union.vars and not initialized.get(word):
                                result.append(st + 1)
                                #print "Suspicious initialization statement:",statement
    return result

def function_declaration(pinst):
    '''
    prototype
        >>> rettype funcname(parameter_list);
    definition
        >>> rettype func(args){
            body
        }
    '''
    proto = {}
    defin = {}
    for prototype in pinst.func_prototypes:
        for line in prototype.text: 
            proto[line.strip()] = prototype.start
    # print proto
    for function in pinst.functions:
        if 'main' in function.text[0].strip():
            continue
        reqtext = function.text[0].strip()
        defin[reqtext.strip('{')] = function.start
    # print defin
    result = []
    if not proto:
        if not defin:
            return result
        for key, items in defin.items():
            result.append(items + 1)
        return result
    else:
        for proto_name, proto_start in proto.items():
            for defin_name, defin_start in defin.items():
                if defin_name in proto_name:
                    if proto_start>defin_start:
                        result_append(defin_start + 1)
    return result

def bitwise_op(pinst):
    ''''''
    bit_op = ['&', '|', '^', '~', '<<', '>>']
    re1 = r'((?P<first>[\w\*\(\)\+-/]+)\s*((&)|(\|)|(\^))\s*(?P<second>[\w\*\(\)\+-/]+))'
    re2 = r'\s*(~)\s*(?P<var>[\w\*\(\)\+-/]+)'
    re3 = r'((?P<first>[\w\*\(\)\+-/]+)\s*((>>)|(<<))\s*(?P<second>[\w\*\(\)\+-/]+))'
    result = []
    for fun in pinst.functions:
        if not fun.vars:
            parse_vars(pinst)
        st = fun.start - 1
        for line in fun.text:
            st += 1
            res1 = re.search(re1, line)
            if res1:
                a = res1.group('first')
                b = res1.group('second')
                if fun.vars.get(a) and fun.vars.get(a)[1] is 0:
                    result.append(st)
                elif fun.vars.get(b) and fun.vars.get(b)[1] is 0:
                    result.append(st)
            res2 = re.search(re2, line)
            if res2:
                var = res2.group('var')
                if fun.vars.get(var) and fun.vars.get(var)[1] is 0:
                    result.append(st)
            res3 = re.search(re3, line)
            if res3:
                a = res3.group('first')
                b = res3.group('second')
                if fun.vars.get(a) and fun.vars.get(a)[1] is 0:
                    result.append(st)
    return result

def verify_sizeof(pinst):
    result = []
    pat = r'\bsizeof\s*\((?P<exp>.*?)\)'
    for function in pinst.functions:
        st = function.start - 1
        lines_list = function.text
        for line in lines_list:
            st += 1
            match = re.search(pat, line)
            if match is None:
                continue
            else:
                exp = match.group('exp')
            if not function.vars:
                parse_vars(pinst)
            if exp in function.vars or exp in bd:
                pass
            else:
                result.append(st + 1)
                #print "invalid sizeof expression, line:",line
    for struct in pinst.structs:
        lines_list = struct.text
        st = struct.start - 1
        for line in lines_list:
            st += 1
            match = re.search(pat, line)
            if match is None:
                continue
            exp = match.group('exp')
            if exp in struct.vars or exp in bd:
                None
            else:
                result.append(st + 1)
                #print "invalid sizeof expression, line:",line
    for union in pinst.unions:
        lines_list = union.text
        st = union.start - 1
        for line in lines_list:
            st += 1
            match = re.search(pat, line)
            if match is None:
                continue
            exp = match.group('exp')
            if exp in union.vars or exp in bd:
                None
            else:
                #print "invalid sizeof expression, line:",line
                result.append(st + 1)
    return result

def parse_function_calls(pinst):
    exclude = ['return', 'for', 'if', 'scanf', 'printf', 'qsort']
    for func in pinst.functions:
        i = 0
        for line in func.text:
            #print line
            f=re.search(r'(?P<fname>\w*)\W*\(.*\)',line)
            if f :
                if i == 0 :
                    i=1
                    func.function_name = f.group('fname')
                    #print 'fvalue',f.group('fname')
                else:
                    y = f.group('fname')
                    if y not in exclude:
                        func.function_calls.append(y)
        #print func.function_name, ' has these function calls :', func.function_calls

def check_recursion(pinst):
    adj = defaultdict(list)
    result = []
    for func in pinst.functions:
        adj[func.function_name] = func.function_calls
    for func in pinst.functions:
        source = func.function_name
        #print 'Source : ',source
        flag=0
        visited = {}
        stack = list()
        stack.append(source)
        while stack:
            cur = stack.pop()
            if visited.get(cur):
                flag=1
                break# cycle detected
            visited[cur] = 1
            for Adj in adj[cur]:
        #        print adj[cur]
                stack.append(Adj)
        func.recursion = flag
        if flag is 1:
            result.append(func.start + 1)
        #print func.function_name,' : ',flag
    return result

def check_switch_condition(pinst):
    pat = r'\bswitch\b\s*\((?P<cond>.*?)\)'
    result = []
    for function in pinst.functions:
        st = function.start -1
        for line in function.text:
            st += 1
            match = re.search(pat, line)
            if match is None:
                continue
            cond = match.group('cond')
            if not ok_switch_condition(cond):
                result.append(st+1)
                #print "switch condition violation, line:", line
    for struct in pinst.structs:
        st = struct.start - 1
        for line in struct.text:
            st += 1
            match = re.search(pat, line)
            if match is None:
                continue
            cond = match.group('cond')
            if not ok_switch_condition(cond):
                result.append(st+1)
                #print "switch condition violation, line:", line
    for union in pinst.unions:
        st = union.start -1
        for line in union.text:
            st += 1
            match = re.search(pat, line)
            if match is None:
                continue
            cond = match.group('cond')
            if not ok_switch_condition(cond):
                result.append(st+1)
                #print "switch condition violation, line:", line


def ok_switch_condition(cond):
    comps = ['==', '!=', '>', '<', '<=', '>=']
    pat = r'.+(' + '|'.join(comps) + ').+'
    return bool(re.search(pat, cond))

def no_star_comments(pinst):
    ''''''
    res = []
    for comment in pinst.global_comments:
        # print comment.text
        text = comment.text[0].strip()
        # print text
        if '/*' in text:
            res.append(text)

    for function in pinst.functions:
        # print function.text
        for line in function.comments:
            text = function.comments[line][0].strip()
            # print text
            if '/*' in text:
                res.append(text)
    return res

def code_commented(pinst):
    ''''''
    res = []
    for fun in pinst.functions:
        for comm in fun.comments:
            text = func.comments[comm]
            
def no_unary_minus(pinst):
    ''''''
    l = []
    for func in pinst.functions:
        for line in func.text:
            if '-' in line:
                a=re.search(r'[((\w+)\))\s*-]', line)
                if(a):
                    pass
                else:
                    check = re.search(r'-(?P<name>\w+)',line)
                    p=check.group('name')
                    if(vars_dict[p][1]==1):
                        l.append(p)
    print l
 
def check_shifts(pinst):
    pat = r'(?P<var>\w+)\s*(<<|>>)\s*(?P<amount>\d+)'
    result = []
    lengths = {
            'int': 32,
            'long long': 64,
            'char': 8,
            'short': 16,
            'long long int': 64,
            'long int': 64,
    }
    for function in pinst.functions:
        if not function.vars:
            parse_vars(pinst)
        st = function.start - 1
        for line in function.text:
            st += 1
            match = re.search(pat, line)
            if match is None:
                continue
            varname = match.group('var')
            amount = int(match.group('amount').strip())
            dtype, unsigned = function.vars[varname]
            max_shift = 32
            if dtype in lengths:
                max_shift = lengths[dtype]
            if amount >= max_shift:
                result.append(st+1)
                #print "max shifts exceeded, line:",line
    for struct in pinst.structs:
        if not struct.vars:
            parse_struct_vars(pinst)
        st = struct.start - 1
        for line in struct.text:
            st += 1
            match = re.search(pat, line)
            if match is None:
                continue
            varname = match.group('var')
            amount = int(match.group('amount').strip())
            dtype, unsigned = struct.vars[varname]
            max_shift = 32
            if dtype in lengths:
                max_shift = lengths[dtype]
            if amount >= max_shift:
                result.append(st+1)
                #print "max shifts exceeded, line:",line
    for union in pinst.unions:
        if not union.vars:
            parse_union_vars(pinst)
        st = union.start - 1
        for line in union.text:
            st += 1
            match = re.search(pat, line)
            if match is None:
                continue
            varname = match.group('var')
            amount = int(match.group('amount').strip())
            dtype, unsigned = union.vars[varname]
            max_shift = 32
            if dtype in lengths:
                max_shift = lengths[dtype]
            if amount >= max_shift:
                result.append(st + 1)
                #print "max shifts exceeded, line:",line
    for gvar in pinst.global_vars:
        # gvar may not be set yet
        line = gvar.text[0]
        st = gvar.start
        match = re.search(pat, line)
        if match is None:
            continue
        varname = match.group('var')
        amount = int(match.group('amount').strip())
        dtype, unsigned = gvar.vars[varname]
        max_shift = 32
        if dtype in lengths:
            max_shift = lengths[dtype]
        if amount >= max_shift:
            result.append(st + 1)
            #print "max shifts exceeded, line:", line
