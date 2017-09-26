# -*- coding: utf-8 -*-
"""
@author: ali_shah_shehzad
"""

"""Finger exercise 13: Implement a function that meets the specification below.
   Use a try-except block."""
   
   
def sumDigits(s):
    """Assumes s is a string
       Returns the sum of the decimal digits in s
       For example is s is 'a2b3c' it returns 5"""
    total = 0
    for i in s:
        try:
            total += int(i)
            print(total)
        except ValueError:
            print("Ignoring exception")
    return total