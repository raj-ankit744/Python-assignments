# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:59:37 2018

@author: user
"""

x = input("Enter a string")
s = "" 
c = 0
for i in x:
    if c%2 == 1:
        s = s + i
    c = c + 1

print(s)

count = dict()
words = x.split()
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)