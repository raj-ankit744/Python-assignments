# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 17:08:58 2018

@author: user
"""
import matplotlib.pyplot as plt
x = [1.45,  2.20,  0.75,  1.23,  1.25,1.25,  3.09,  1.99,  2.00,  0.78,1.32 , 2.25,  3.15,  3.85,  0.52,0.99  ,1.38  ,1.75 , 1.22 , 1.75]
plt.hist(x)
plt.xlabel('Price(in dollars)')
plt.ylabel('Frequency')
plt.show()