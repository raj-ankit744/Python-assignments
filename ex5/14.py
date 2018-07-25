# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:53:45 2018

@author: user
"""

x, y = input("Enter the path of the file to be copied\n"), input("Enter the path of the second file\n")
try:
    with open(x, 'r') as copy, open(y, 'a') as paste:
        l = [i for i in copy]
        paste.writelines(l)
        copy.close()
        paste.close()
except IOError as e:
    print("Operations failed ", e.strerror)

print("copied successfully")