import re
import collections
import zlib
import base64

class Splitter:

    text = None
    def __init__(self, text):
        """
        txt here is the c program that we need to split here
        """
        self.text = text

    def is_preprocessor(self):
        pass


class Line:

    def __init__(self, line):
        self.line = line

    def fetch_header_file(self):
        """ Given that it's an include statement """
        header = None
        try:
            header = re.findall('<(.*)>', self.line)[0]
        except IndexError:
            header = re.findall('"(.*)"', self.line)[0]
        except:
            # raise Exception("")
            return -1
        return header[:-2] # return without extension
    
    def is_preprocessor(self):
        """ 
        If the line starts with a '#' it must be a preprocessor
        """
        if self.line.startswith('#'):
            if self.line.startswith('#include'):
                header_file = self.fetch_header_file()
                if not header_file in store['header_files']:
                    raise Exception("Header file is not valid")
            # Other possibilities
            return 1 # it's a preprocessor
        else:
            return 0  # it's not a preprocessor


header_files = "eNotjlsOwzAIBC+0n1XuQxziUGETAenj9o2t/uyMxJMi2BPF2qn8QcnvyWD3bti5v7CrUUJ6jkJAwpbHApUmGVArpIxGeSA4n+1ESO2kiNxIb53idSKtSRm2ms2OjfeBe/mEjVRZB7o55+Vj3qVXZJ1H8nCmLZDSGFc5yPH+5/jvB7mfTyQ="

keywords = "eNotTlGSQyEIO8z75VJU0ceshY5C293Tb3ztDCYwJJijSlMTOmRo27h2b3UPnwfBJvuwlZEVknGZHpP7nenIa8sZTrcp/EOFcaecPKm4rdgYaikEHecIqo7K2xC6vhTLO8k7ZBq14RzUfFJ3HEQKtaDh1mlK1wURmkhI1+kzaGk3qaA/8UYrOLSAZhbsXhrlpPh9yI6Ypm7Ar+XpumHAgSSvE/gPTTtk7g=="

decode = lambda encoded: zlib.decompress(base64.b64decode(encoded))
keywords = decode(keywords).split(',')
header_files = decode(header_files).split(',')
print keywords
print header_files
store = collections.defaultdict(list)

store['keywords'] = keywords # To keep track of validity of variables
store['line_breaks'] = ['\n'] # To split the entire program to work 
store['statement_breaks'] = [',', ';', '}']
store['header_files'] = header_files


