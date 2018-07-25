# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:14:37 2018

@author: user
"""

x = input("Enter the path of the file to be read\n")
file = open(x, 'r')
print("The file reads as: \n")
line = file.readline()
while(line!=""):
    print(line)
    line = file.readline()

file.close()
