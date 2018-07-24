# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:09:57 2018

@author: user
"""
l = [1,4,5,3,6,7,3,7]
m = max(l)
print("largest Element: ", m)
print("second largest Element: ", max(i for i in l if i<m))
l[0],l[-1] = l[-1],l[0]
print(l)