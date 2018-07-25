# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:49:05 2018

@author: user
"""

x = input("Enter the path of a file: ")
'''try:
    l = []
    with open(x, 'r') as file:
        l = list(''.join([i for i in file]))
        #print(l)
        l = ''.join([l[i].upper() if (True if i == 0 or l[i-1] == ' ' or l[i-1] == '\n' else False) else l[i] for i in range(len(l))])
    file.close()
    with open(x, 'w') as file:
        file.write(l)
    file.close()
except IOError as e:
    print("Operation failed : ",e.strerror)
print("Operation successful")'''

f=open(x,"r")
con=f.read()
print(con.title())