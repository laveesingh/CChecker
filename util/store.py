import zlib
import base64


### Global Properties go here
c_program = None  # the main c program as a string
flags = none  # specification flags
store = none  # dictionary to store runtime details
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

keywords = decode(KEYWORDS).split(',')
header = decode(HEADER).split(',')
store = dict()  # Stores major details of program
functions = dict()
store['keywords'] = keywords
store['header'] = header
