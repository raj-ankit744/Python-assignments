# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:12:57 2018

@author: user
"""
x = input("Enter a String")
x = list(x)
x.sort()
x = "".join(x)
print(x)