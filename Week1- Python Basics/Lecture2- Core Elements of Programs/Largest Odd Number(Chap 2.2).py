# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 03:10:48 2017

@author: ali_shehzad
"""

"""Finger exercise 2: 
Write a program that examines three variables—x, y, and z—and prints the largest
odd number among them. If none of them are odd, it should print a message to that effect
"""


print("Input 3 numbers and we'll output the largest of those odd numbers")

x=int(input("Num1: "))
y=int(input("Num2: "))
z=int(input("Num3: "))

if x%2==0 and y%2==0 and z%2==0: #check if all of the numbers provided are even.
    print("No odd numbers provided.") 
elif x%2==0 and y%2==0: #check if x and y are even.
    print(z, "is the largest odd number.") #if above statement is true, z is the only odd num hence it's the largest.
elif x%2==0 and z%2==0: #check if x and z are even. 
    print(y, "is the largest odd number.") #if above statement is true, y is the only odd num hence it's the largest.
elif y%2==0 and z%2==0: #check if y and z are even. 
    print(x, "is the largest odd number.") #if above statement is true, x is the only odd num hence it's the largest.
elif x%2==0: #check if x is even
    if y>z: #if above statement is true, we only have to compare y and z now.
        print(y, "is the largest odd number.")
    else:
        print(z, "is the largest odd number.")
elif y%2==0: #check if y is even
    if x>z: #if above statement is true, we only have to compare x and z now.
        print(x, "is the largest odd number.")
    else:
        print(z, "is the largest odd number.")
elif z%2==0: #check if z is even
    if x>y: #if above statement is true, we only have to compare x and y now.
        print(x, "is the largest odd number.")
    else:
        print(y, "is the largest odd number.")
else: #all 3 numbers are odd so we'll compare all 3 of them
    if x>y and x>z:
        print(x, "is the largest odd number.")
    elif y>z:
        print(y, "is the largest odd number.")
    else:
        print(z, "is the largest odd number.")
            
        
