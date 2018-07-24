# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:26:01 2018

@author: user
"""
import math
r = int(input("Enter range"))
print([i for i in range(r+1) if int(math.sqrt(i))**2 == i])
print([i for i in range(r+1) if sum(int(digit) for digit in str(i))<10])