"""
Introduction to Computation and Programming Using Python
3.1 Finger exercise | page 23
Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6
and root ** pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a
message to that effect.
"""


x = int(input("Please enter an integer greater than 1: "))
root = 1
pwr = 2

while root ** pwr != (x) and root < (x):
    while pwr < 6 and root ** pwr != (x):
        pwr = pwr + 1
    if root ** pwr != (x):
        root = root + 1
        pwr = 2
if root ** pwr == (x):
    print (str(root) + " ** " + str(pwr) + " = " + str(x))
else:
    print("No root/pwr pair exists for this integer between the given range.")
        
            
