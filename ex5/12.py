# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:33:49 2018

@author: user
"""

import collections
x, y = input("Enter the path of the file: \n"), input("Enter a letter")
try:
    with open(x, 'r') as f:
        l = list(''.join([i for i in f if i.strip()]))
        lettercount = collections.Counter(l)
    f.close()
except IOError as e:
    print("operation failed: ",e.strerror)
#print(lettercount)
print("The count of letter '",y,"' is ",lettercount[y])