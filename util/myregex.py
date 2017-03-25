'''
This file contains same methods as re module, but these methods are modified a
little bit in order to avoid spoilers that may arise due to double quoted
strings in the text.
For example:
    printf("value of a = ", 5);
'=' sign in the line above, may spoil patterns created to detect assignments
only.

'''
import re


# following functions find a given pattern, excluding the text given in the
# double quotes(").


def search_wq(pat, text, flags=0):
    """
        Equivalent to re.search, but ignores text inside quotes as string.
    """
    text = re.sub(r'\"(.*?)\"', '', text)
    return re.search(pat, text, flags)


def match_wq(pat, text, flags=0):
    """
        Equivalent to re.match, but ignores text inside quotes as string.
    """
    text = re.sub(r'\"(.*?)\"', '', text)
    return re.match(pat, text, flags)


def split_wq(pat, text, maxsplit=0, flags=0):
    """
        Equivalent to re.split, but ignores text inside quotes as string.
    """
    text = re.sub(r'\"(.*?)\"', '', text)
    return re.split(pat, text, maxsplit, flags)


def findall_wq(pat, text, flags=0):
    """
        Equivalent to re.findall, but ignores text inside quotes as string.
    """
    text = re.sub(r'\"(.*?)\"', '', text)
    return re.findall(pat, text, flags)


def finditer_wq(pat, text, flags=0):
    """
        Equivalent to re.finditer, but ignores text inside quotes as string.
    """
    text = re.sub(r'\"(.*?)\"', '', text)
    return re.findter(pat, text, flags)
