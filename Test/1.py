# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:11:16 2018

@author: user
"""

import pandas as pd
df = pd.read_csv("C:/Users/user/Desktop/ARG/Test/100 Sales Records.csv")
print("The names of the columns are",df.columns.tolist())
print()
print(df.iloc[:10,:10])

d = df['Total Profit']

ax = d.plot(kind = 'bar')
ax.set_xlabel('Index')
ax.set_ylabel('Price')
print('Item type of product whose Total cost > 1000000')
print(df.loc[df['Total Cost'] > 1000000]['Item Type'])