# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:12:04 2018

@author: user
"""
print([x for x in range(1,1000) if str(x) == str(sum(int(i)**len(str(x)) for i in str(x)))])
print(list(filter(lambda x: str(x) == str(sum(int(i)**len(str(x)) for i in str(x))), [i for i in range(1,1001)])))