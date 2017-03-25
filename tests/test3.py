import re


pattern = r'((?P<ret>[a-zA-Z_]\w*)\*?\s+\*?(?P<name>[a-zA-Z_]\w*)\s*' +\
        r'\(.*\)\s*\;)'

text = "int* summation (int a, int b) ;"

print re.search(pattern, text)
