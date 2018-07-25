# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:39:20 2018

@author: user
"""

x = input("Enter the path of the file: \n")
try:
    with open(x, 'r') as file:
        l = ' '.join([i for i in file])
        count = sum(1 for i in l if i == ' ')
        file.close()
except IOError as e:
    print("Operation failed :", e.strerror)
print("no. of blank spaces : ", count)