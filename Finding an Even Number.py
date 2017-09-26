# -*- coding: utf-8 -*-
"""
@author: ali_shah_shehzad
"""

"""Finger Exercise 13: Implement a function that satisfies the specification."""

def findAnEven(L):
    """Assumes L is a list of integers
       Returns the first even number in L
       Raises Value error if L does not contain an even number."""
       
    for num in L:
        if num%2 == 0:
            return num
    raise ValueError("No even number in the list.")