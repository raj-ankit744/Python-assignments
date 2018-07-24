# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:43:04 2018

@author: user
"""

x = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
k = '*'.join([str(k1) for k1 in x.keys()])
v = '*'.join([str(v1) for v1 in x.values()])
print("product of keys ",eval(k))
print("product of values ", eval(v))
