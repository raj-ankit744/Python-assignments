# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 14:02:27 2018

@author: user
"""
import matplotlib.pyplot as plt
import pandas
def pred(b0,b1,x):
    return b0+b1*x

def cost_func(x,y,b1,b0):
    n = len(x)
    error = 0.0
    for i in range(n):
        error += (y[i] - pred(b0,b1,x[i]))**2
    return error/n

def update(x,y,b1,b0,lr):
    new_b1 = 0
    new_b0 = 0
    n = len(x)
    for i in range(n):
        new_b1 += -2.0*x[i]*(y[i] - pred(b0,b1,x[i]))
        new_b0 += -2.0*(y[i] - pred(b0,b1,x[i]))
    b1 -= lr*new_b1/n
    b0 -= lr*new_b0/n
    return b1,b0

df = pandas.read_csv("employee_data.csv")
x = df['Experience in years'].values.tolist()
y = df['Salary'].values.tolist()
b0 = 0.0
b1 = 0.0
cost_log = []
for i in range(1000):
    b1,b0 = update(x,y,b1,b0,0.01)
    cost = cost_func(x,y,b1,b0)
    cost_log.append(cost)
print(cost_log[0],"->",cost_log[-1])
plt.scatter(x,y)
y_pred = [b0 + b1*i for i in x]
#print(y_pred)
plt.plot(x,y_pred)
plt.show()