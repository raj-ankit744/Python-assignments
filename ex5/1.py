# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:49:15 2018

@author: user
"""

s = input("Enter a String")
x = set("AEIOUaeiou")
print(len([i for i in s if i in x]))
