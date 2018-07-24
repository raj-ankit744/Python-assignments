# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:29:16 2018

@author: user
"""
def count_char(x):
    sum = 0
    for i in x:
        if i.isalpha():
            sum = sum + 1
    return sum

def count_num(x):
    sum = 0
    for i in x:
        if i.isnumeric():
            sum = sum + 1
    return sum

def count_lower(x):
    sum = 0
    for i in x:
        if i.islower():
            sum = sum + 1
    return sum

def count_upper(x):
    sum = 0
    for i in x:
        if i.isupper():
            sum = sum + 1
    return sum

x = input("Enter a String")
print("no. of characters: ", count_char(x))
print("no. of digits :", count_num(x))
print("no. of upper letters:", count_upper(x))
print("no. of lower letters:", count_lower(x))
print("length of string", len(x))
x = x + 'ing'
print(x)
y = x[0]
x = x.replace(y,"$")
x = list(x)
x[0] = y
x = "".join(x)
print("modified string", x)