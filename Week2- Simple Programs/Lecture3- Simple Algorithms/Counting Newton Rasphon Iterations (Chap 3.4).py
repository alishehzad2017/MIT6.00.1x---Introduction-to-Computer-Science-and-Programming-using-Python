# -*- coding: utf-8 -*-
"""
@author: ali_shehzad
"""

#Newton-Rasphon for square root
#Find x such that x**2 - 24 is within epsilon of 0

"""
Finger exercise 10: Add some code to the implementation of Newton-Raphson that keeps track of the
number of iterations used to find the root. Use that code as part of a program that compares the
efficiency of Newton-Raphson and bisection search. (You should discover that Newton-Raphson is
more efficient.)
"""

epsilon = 0.01
k = 123456789
guess = k/2.0
iteration = 0

while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    iteration += 1
    print("Iternation no: " + str(iteration))

print("Square root of", k, "is about", guess)
