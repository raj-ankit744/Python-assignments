# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:10:04 2018

@author: user
"""
def isarmstrong(x):
    l = len(x)
    sum = 0
    for i in x:
        sum = sum + int(i)**l
    if str(sum) == x:
        return True
    return False

x = input("Enter a no.")
print(isarmstrong(x))
