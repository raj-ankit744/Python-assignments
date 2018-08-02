# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:44:20 2018

@author: user
"""
import statistics as st, pandas as pd, matplotlib.pyplot as plt,math 
df = pd.read_csv("C:/Users/user/Desktop/ARG/week 2 ex 2/headbrain.csv")
x = df['Head Size(cm^3)'].tolist()
y = df['Brain Weight(grams)'].tolist()
plt.scatter(x,y)
plt.show()
c = tuple(zip(x, y))
mx = st.mean([xi for xi,yi in c])
my = st.mean([yi for xi,yi in c])

cov = (sum([(xi - mx)*(yi - my) for xi,yi in c]))
sd = (sum([(xi-mx)**2 for xi,yi in c]))
B1 = cov/sd
B0 = my - (cov/sd)*mx
print("B1 = ",B1)
print("B0 = ",B0)
ssres = sum([(yi-(B0 + B1*xi))**2 for xi,yi in c])
rmse = math.sqrt(ssres/len(x))
print("Ei^2 = ",rmse)
R2 = 1 - (ssres)/sum([(yi-my)**2 for xi,yi in c])
print("R2 = ",R2)

