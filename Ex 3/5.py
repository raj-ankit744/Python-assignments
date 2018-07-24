# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:54:40 2018

@author: user
"""

import collections
l = [1,2,43,5,66,7,54,6,7,3,4,5]
print(collections.Counter(l))
print("largest even no. ",max(i for i in l if i%2 == 0))
print("largest odd no. ",max(i for i in l if i%2 == 1))