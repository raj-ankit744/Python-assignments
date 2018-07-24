# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:31:50 2018

@author: user
"""
import operator
student = dict()
student = dict(input("Enter Name and Marks:\n").split() for i in range(10))
print(student)
student = sorted(student.items(), key = operator.itemgetter(1))
print(student)