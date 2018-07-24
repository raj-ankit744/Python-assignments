# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:55:40 2018

@author: user
"""

x = input("Enter a String")
x = list(x)
u = x[0]
x[0] = x[-1]
x[-1] = u
x = "".join(x)
print(x)