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

HEADER = "eNotjlsOwzAIBC+0n1XuQxziUGETAenj9o2t/uyMxJMi2BPF2qn8QcnvyWD3b\
                ti5v7CrUUJ6jkJAwpbHApUmGVArpIxGeSA4n+1ESO2kiNxIb53idSKtSRm2ms\
                2OjfeBe/mEjVRZB7o55+Vj3qVXZJ1H8nCmLZDSGFc5yPH+5/jvB7mfTyQ="
KEYWORDS = "eNotTlGSQyEIO8z75VJU0ceshY5C293Tb3ztDCYwJJijSlMTOmRo27h2b3UPnwfBJ\
            vuwlZEVknGZHpP7nenIa8sZTrcp/EOFcaecPKm4rdgYaikEHecIqo7K2xC6vhTLO8\
            k7ZBq14RzUfFJ3HEQKtaDh1mlK1wURmkhI1+kzaGk3qaA/8UYrOLSAZhbsXhrlpPh\
            9yI6Ypm7Ar+XpumHAgSSvE/gPTTtk7g=="
KEYWORDS = decode(KEYWORDS).split(',')
HEADER = decode(HEADER).split(',')
STORE = dict()  # Stores major details of program
STORE['KEYWORDS'] = KEYWORDS
STORE['HEADER'] = HEADER

#print KEYWORDS
