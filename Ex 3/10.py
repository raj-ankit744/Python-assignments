# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:35:47 2018

@author: user
"""

l = [1,2,3,4,56,4,8,63,2,5,6,6]
print([sum(l[0:x+1]) for x in range(len(l))])