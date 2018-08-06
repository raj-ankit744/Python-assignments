# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:06:22 2018

@author: user
"""
import operator
file = "C:/Users/user/Desktop/ARG/Test/Input.txt"
students = []
with open(file,'r') as f:
    x = f.readline()
    while(x!=""):
        students.append(tuple(x.split()))
        x = f.readline()
f.close()
print()
students = sorted(students, key = operator.itemgetter(3))
for i in range(len(students)):
    print("{:10}{:5}{:10}{:5}{:5}".format(students[i][0],students[i][1],students[i][2],students[i][3],students[i][4]))
bmi = []
for i in students:
    x = float(i[4])/float(i[3])**2
    bmi.append(x)
print()
for i in range(len(students)):
    print("{:10}{:5}{:10}{:5}{:5}{:5}".format(students[i][0],students[i][1],students[i][2],students[i][3],students[i][4],bmi[i]))

healthy = []
overweight = []
obese = []

for i in range(len(bmi)):
    if bmi[i] >= 30:
        obese.append(i)
    elif bmi[i] >=25:
        overweight.append(i)
    else:
        healthy.append(i)
print()
print("Healthy Students")
for i in healthy:
    print(students[i][0])
print()
print("Overweight Students")    
for i in overweight:
    print(students[i][0])
print()
print("Obese Students")
for i in obese:
    print(students[i][0])