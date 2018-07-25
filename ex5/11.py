# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:22:30 2018

@author: user
"""

x, y = input("Enter the path of the file to be copied"), input("Enter the path of the file to write")
try:
    with open(x, 'r') as copy, open(y, 'w') as paste:
        lines = [l for l in copy]
        paste.writelines(lines)
    copy.close()
    paste.close()
except IOError as e:
    print("operation failed: ",e.strerror)
print("Successfully copied")