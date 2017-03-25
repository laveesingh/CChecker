import zlib
import base64


### Global Properties go here
C_PROGRAM = None  # the main c program as a string
FLAGS = None  # specification flags
STORE = None  # dictionary to store runtime details
KEYWORDS = None  # list of all keywords
HEADER = None  # list of all header files


def decode(encoded):
    """
        takes a base64 encoded compressed string, decodes it, then\
                decompresses it and returns it.
        >>> decode(encoded_string) -> decode and decompress it
    """
    decoded = base64.b64decode(encoded)
    return zlib.decompress(decoded)

HEADER = ['assert', 'complex', 'ctype', 'errno', 'fenv', 'float', 'inttypes', 'iso646', 'limits', 'locale', 'math', 'setjmp', 'signal', 'stdalign', 'stdarg', 'stdatomic', 'stdbool', 'stddef', 'stdint', 'stdio', 'stdlib', 'stdnoreturn', 'string', 'tgmath', 'threads', 'time', 'uchar', 'wchar', 'wctype']
KEYWORDS = ['#define', '#elif', '#else', '#endif', '#if', '#ifdef', '#ifndef', '#include', '#line', '#pragma', '#undef', 'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']

KEYWORDS = decode(KEYWORDS).split(',')
HEADER = decode(HEADER).split(',')
STORE = dict()  # Stores major details of program
STORE['KEYWORDS'] = KEYWORDS
STORE['HEADER'] = HEADER

print "HEADER =", HEADER
print "KEYWORDS =", KEYWORDS
