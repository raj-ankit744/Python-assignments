# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:29:35 2018

@author: user
"""

x = input("Enter group of words separated by ','")
x = x.split(",")
s = set()
for i in x:
    s.add(i)
print(s)