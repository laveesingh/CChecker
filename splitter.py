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
