# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:10:28 2018

@author: user
"""

d1 = {81570: 'Ankit', 81573: 'praful', 81572: 'manjunath', 81598: 'monodeep'}
k = 81570
if k in d1.keys():
    print("key, value => ",str(k)+","+str(d1[k]))
else:
    print("key not found")