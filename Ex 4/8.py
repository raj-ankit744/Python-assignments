# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:28:06 2018

@author: user
"""
x = input("Enter a string")
count = dict()
words = x.split()
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)