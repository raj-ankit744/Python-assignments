# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 15:58:31 2018

@author: user
"""

x = input("Enter the path of the file: ")
f=open(x,"r")
con  = f.read()
print("".join([con[len(con) - i -1] for i in range(len(con))]))
'''
try:
    with open(x, 'r') as file:
        l = ("".join([i for i in file])).split()     l = ["".join(reversed(i)) for i in l]
    file.close()
   
    '''