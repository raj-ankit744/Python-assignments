# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:06:37 2018

@author: user
"""
import random
l = []
for i in range(10):
    x = random.randint(1,11)
    l.append((x,x*x))

print(l)
l.sort()
print(l)