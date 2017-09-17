# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 03:10:48 2017

@author: ali_shah_shehzad
"""

"""
Finger exercise 3: 
Replace the comment in the following code with a while loop.
numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
concatenate X to toPrint numXs times
print(toPrint)
"""

numXs=int(input("How many times should I print the letter X? "))
toPrint=""
itersLeft=numXs
while itersLeft != 0:
    toPrint += 'X'
    itersLeft -= 1
print(toPrint)