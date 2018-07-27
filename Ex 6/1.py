# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:26:34 2018

@author: user
"""
import numpy
a = numpy.array([['Rhia',10,20,30,40,50],
           ['Alan',75,80,75,85,100],
           ['Smith',80,80,80,90,95]])

#print([i[:2] for i in (j for j in a)])
print(a[:3,:2])
l = ['Sam',82,79,88,97,99]
a[2] = l
print(a)
a[0][3] = 95
print(a)
l = numpy.array([[73], [80], [85]])
print(numpy.append(a, l, axis = 1))
