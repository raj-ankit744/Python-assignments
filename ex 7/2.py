# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:23:03 2018

@author: user
"""
import numpy
A = numpy.array([[3, 5, 6],
		    [4, 8, 10],
		    [2, 1, 8]])
I = numpy.array([[1, 0, 0],
    [0, 1, 0],
	[0, 0, 1]])

print("proved" if numpy.array_equal(A,numpy.dot(A,I)) else "not proved")