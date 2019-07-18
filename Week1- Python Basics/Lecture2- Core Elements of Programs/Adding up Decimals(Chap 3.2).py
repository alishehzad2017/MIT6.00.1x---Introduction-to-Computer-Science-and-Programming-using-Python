# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 03:10:48 2017

@author: ali_shehzad
"""

"""
Finger exercise 5:
Let s be a string that contains a sequence of decimal numbers separated by commas,
e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s.
"""


total = 0
s = input("Please enter a string of sequence of decimal numbers: ")
for c in s.split(","): #split 's' creating a list with each decimal number as it's element
    total += float(c)
print(total)
