# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:02:48 2018

@author: user
"""
import numpy as np
a = np.array([[1,2,3,4,5], [1,2,3,4,5], [3,4,5,6,7], [6,4,7,3,7]])
print("Dimensions of 2D array: ",a.shape)

a = a.reshape(2,2,5)

print("new 3D array\n",a)
print("\n\n")
print("Adding 5\n\n")
a = a + 5
print(a)
print("\n\n")
print("Subtracting 2\n\n")
a = a - 2
print(a)
print("\n\n")
print("Multiplying 5\n\n")
a = a * 5
print(a)