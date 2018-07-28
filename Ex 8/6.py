# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:32:53 2018

@author: user
"""
import re
p = input("Enter password: ")

x = r'(^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9])[A-Za-z\d$@$!%*?&]){8,14}'
if re.match(r'[^A-Z]',p) or re.match(r'[^0-9]',p) and len(p)<8 or len(p)>14:
#if re.match(y,p):
    print("invalid password") 
else:
    print("valid password")
   