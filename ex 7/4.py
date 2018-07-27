# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:35:13 2018

@author: user
"""
import re
x = input("Enter String: ")
print(len(re.findall('[A-Za-z]',x)))
print(len(re.findall('[0-9]',x)))