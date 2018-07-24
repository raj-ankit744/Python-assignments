# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:16:26 2018

@author: user
"""

def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        z = (fibonacci(x-1) + fibonacci(x-2))
        return z

def factorial(x):
    if x<=1:
        return 1
    return x*factorial(x-1)

x = int(input("Enter a no.\n"))
print("factorial : ", factorial(x))
print("fibonacci : ", fibonacci(x))