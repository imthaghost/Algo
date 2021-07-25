


import collections
from typing import Collection


def first_uniq_char(s : str) -> int: 
    seen = collections.Counter(s)
   
    for idx, letter in enumerate(s):
        if seen[letter] == 1:
            return idx
    return -1