# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:10:00 2018

@author: user
"""
x = input("Enter a String")
if len(x)%4 == 0:
    x = "".join(reversed(x))
print(x)