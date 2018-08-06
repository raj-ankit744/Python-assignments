# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:37:16 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/user/Desktop/ARG/Test/camera.csv")
col = df.columns.tolist()
print("The names of the columns are\n",col)
d1 = df.iloc[0,:].tolist()
print()
print('Data types:\n')
print(tuple(zip(d1,col)))
print('\n\n')

for i in range(1,26):
    print("{:3} {:30}{:30}{:30}".format(i,df['Model'].iloc[i],df['Release date'].iloc[i],df['Price'].iloc[i]))
print("Summary of whole dataset")
d = df.iloc[1:,2:].astype(float)
print(df.iloc[1:,0].describe())
print(d.describe())
print('\n\n')
print("Summary of price ")
pr = df['Price'].iloc[1:].astype(float)
print(pr.describe())
print()
index = pd.DatetimeIndex(df['Release date'].iloc[1:].tolist())
#dx = pd.DataFrame(d,index=index)
#dx = pd.DataFrame(d.loc[d['Price'] > 1000]['Price'].tolist())
#print(dx)
plt.scatter(index,d['Price'])
plt.xlabel('Time')
plt.ylabel('Price')
plt.show()


