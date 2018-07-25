# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:24:35 2018

@author: user
"""

x = input("Enter the path of the file\n")
file = open(x, 'r')
line = file.readline()
count = 0
while(line != ""):
    #print(line.strip().split())
    count += len(line.strip().split())
    line = file.readline()

file.close()
print(count)