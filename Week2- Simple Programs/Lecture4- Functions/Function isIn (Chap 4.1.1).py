# -*- coding: utf-8 -*-
"""
@author: ali_shah_shehzad
"""

"""
Finger exercise 11: Write a function isIn that accepts two strings as
arguments and returns True if either string occurs anywhere in the other,
and False otherwise. Hint: you might want to use the built-in str
operation in.
"""


def isIn(str1, str2):
    if len(str1) > len(str2): #We're comparing which string is longer and then checking to see
        if str2 in str1:      #if the shorter string is present in the longer string
            return True
    else:
        if str1 in str2:
            return True
    return False