# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:18:50 2018

@author: user
"""
x = input("Enter a string")
c = input("enter a character")
print([pos for pos, char in enumerate(x) if char == c])
c = 0
x = x.lower()
for i in x:
    if i=='a' or i=='e' or i == 'i' or i == 'o' or i == 'u':
        c = c + 1
print("count", c)
