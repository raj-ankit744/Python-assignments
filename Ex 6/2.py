# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:56:41 2018

@author: user
"""
import re, collections  
a = "#Python is an interpreted high level programming language for general-purpose programming*."
b = re.sub("[^A-Za-z0-9 ]+","",a)
print(b)
print(list(filter(lambda x: x == x[::-1], a.split())))
d = dict(collections.Counter(b.split()))
d = list(zip(d.keys(),d.values()))
x = dict(filter(lambda x: x[1]>1,d))
print(x)