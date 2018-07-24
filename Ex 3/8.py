# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:19:12 2018

@author: user
"""

import numpy
l = input("Enter List of coefficients separated by spaces").split()
l.sort()
print(numpy.roots(l))