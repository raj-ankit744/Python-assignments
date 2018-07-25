# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:01:15 2018

@author: user
"""
import collections
x, y = input("Enter the path of the file\n"), input("Enter a word: \n")
wordscount = dict()
with open(x, 'r') as file:
    words = (' '.join([' '.join(i.split()) for i in file if i.strip()])).split()
    wordscount = collections.Counter(words)
file.close()
print(wordscount)
print("No. of occurences of ",y, " is ", wordscount[y])