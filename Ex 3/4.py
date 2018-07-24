# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:50:36 2018

@author: user
"""

l = [1,2,43,5,66,7,54,6,7,3,4,5]
print("3rd element ",l[2])
print("6th element ", l[5])
print("first five elements ", l[:5])
print("Elements 7 to end ", l[7:])
l[1] = 'x'
l[4] = 'y'
del l[4]
print(l)
print("no. of elements " ,len(l))