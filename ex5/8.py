# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:24:35 2018

@author: user
"""

x = input("Enter the path of the file\n")
'''
with open(x) as f:
    print(sum(1 for line in f if line.strip()))
    '''
f=open(x,"r")
con=f.read()
print(con.count('\n'))
f.close()
