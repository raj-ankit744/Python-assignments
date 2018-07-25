# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:51:06 2018

@author: user
"""

x, y = input("Enter the path of the file: \n"), input("Enter the string to append:\n")
with open(x, 'a') as f:
    f.write(y)
f.close()