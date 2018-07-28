# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:12:35 2018

@author: user
"""
n = int(input("Enter no. of entries: "))
x = [(float(input("Enter Student's height in m: ")), float(input("Enter student's weight in kg: "))) for i in range(n)]
print("list of BMI: ")
print([j/(i*i) for i,j in x])