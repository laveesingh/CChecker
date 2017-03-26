'''
This program checks extents(from starting point till ending point) of various
components of the program. Components include: functions, loops, conditionals,
structs, etc.
'''
import re

from store import counterparts
from utilities import statement

def preprocessors(name, lines_list, index):
    '''
    Function returns index of the ending line of the preprocessor
    '''
    one_liners = ['define', 'include', 'line', 'pragma']
    if name in one_liners:
        return index
    if statement(lines_list[index]).is_preprocessor():
        thisname = re.search(r'\#(?P<name>\w+)', ).group('name')
        if thisname == counterparts[name]:
            return index
        thisend = preprocessors(thisname, lines_list, index)
        return preprocessors(name, lines_list, thisend+1)

