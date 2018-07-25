# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:44:59 2018

@author: user
"""
x = input("Enter the path of the file\n")
try:
    with open(x, 'r') as file:
        l = list(''.join([i for line in file for i in line if i.isnumeric()]))
    file.close()
except IOError as e:
    print("operation failed ", e.strerror)
print("list of numbers: ",l)  