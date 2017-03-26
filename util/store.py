import zlib
import base64
import sys

# disable creation of *.pyc files
sys.dont_write_bytecode = True

### Global Properties go here
c_program = None  # the main c program as a string
flags = None  # specification flags
store = None  # dictionary to store runtime details
keywords = None  # list of all keywords
header = None  # list of all header files


header = [
        'assert'
        'complex',
        'ctype',
        'errno',
        'fenv',
        'float',
        'inttypes',
        'iso646',
        'limits',
        'locale',
        'math',
        'setjmp',
        'signal',
        'stdalign',
        'stdarg',
        'stdatomic',
        'stdbool',
        'stddef',
        'stdint',
        'stdio',
        'stdlib',
        'stdnoreturn',
        'string',
        'tgmath',
        'threads',
        'time',
        'uchar',
        'wchar',
        'wctype'
]

keywords = [
        '#define',
        '#elif',
        '#else',
        '#endif',
        '#if',
        '#ifdef',
        '#ifndef',
        '#include',
        '#line',
        '#pragma',
        '#undef',
        'auto',
        'break',
        'case',
        'char',
        'const',
        'continue',
        'default',
        'do',
        'double',
        'else',
        'enum',
        'extern',
        'float',
        'for',
        'goto',
        'if',
        'int',
        'long',
        'register',
        'return',
        'short',
        'signed',
        'sizeof',
        'static',
        'struct',
        'switch',
        'typedef',
        'union',
        'unsigned',
        'void',
        'volatile',
        'while'
]

datatypes = [
        'int',
        'float',
        'double',
        'char',
        'void'
]

store = dict()  # Stores major details of program
functions = dict()
store['keywords'] = keywords
store['header'] = header
