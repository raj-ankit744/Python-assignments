# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 16:07:29 2018

@author: user
"""
import math
x, y = int(input("Enter lower range: ")), int(input("Enter higher range: "))
l = [num for num in range(x,y+1) if all([(num % i != 0) for i in range(2,int(math.sqrt(num))+1)])]
print(l)
l = [str(i) for i in l]
print(list(filter(lambda x: x == x[::-1],l)))