# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:28:34 2018

@author: user
"""

s = input("Enter a string").split()
l = []
for x in s:
    l.append(x[0])

d = dict()
d = dict(zip(l,s))
print(d)