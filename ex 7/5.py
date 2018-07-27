# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:53:40 2018

@author: user
"""
import math,sys
def fun1():
    x, y = int(input("Enter first no: ")), int(input("Enter second no."))
    gcd  =  math.gcd(x, y)
    print("The gcd of two nos. is ",gcd)
 
def fun2():
    x, y = int(input("Enter first no: ")), int(input("Enter second no."))
    gcd  =  math.gcd(x, y)
    lcm = (x*y)/(gcd)
    print("The lcm of two nos. is ",lcm)

def fun3():
    x = int(input("enter a no."))
    print("The factorial of the no. is : ", math.factorial(x))

def fun4():
    x = int(input("Enter a no.: "))
    print([i for i in range(1,x/2) if x%i == 0])

def fun5():
    sys.exit("Thank you for using our calculator")
d = {'1':fun1, '2':fun2, '3':fun3, '4':fun4, '5': fun5}
while(True):
    print("1. Find GCD\n 2. Find LCM\n 3. Find factorial\n 4. Find factors\n 5. Exit\n")
    x = input("enter choice: ")
    d[x]()

