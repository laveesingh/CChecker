import zlib
import base64
import sys

# disable creation of *.pyc files
sys.dont_write_bytecode = True

### Global Properties go here
c_program = None  # the main c program as a string
flags = None  # specification flags
root = None  # dictionary to store runtime details
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

builtin_datatypes = [
        'int',
        'float',
        'double',
        'char',
        'void',
        'long long',
        'long',
        'short',
        'bool',
        'int8',
        'int16'
        'int32',
        'int64',
        'int8_t',
        'int16_t'
        'int32_t',
        'int64_t',
        'size_t',
]

extended_datatypes = [
        'unsigned int',
        ]  # TODO: More to be added

root = dict()  # Stores major details of program
functions = dict()
root['keywords'] = keywords
root['header'] = header
counterparts = {
        'define': '',
        'include': '',
        'undef': '',
        'ifdef': 'endif',
        'ifndef':'endif',
        'if': 'endif',
        'elif': 'endif',
        'else': 'endif',
        'error': '',
        'pragma':''
}

