# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 09:57:22 2018

@author: user
"""

import pandas as pd,matplotlib.pyplot as plt
df = pd.read_excel("C:/Users/user/Desktop/ARG/week 2 ex 2/ca_result.xlsx", header = [0,1])
df.index = pd.to_datetime(df.index)
appear1 = df['Group I']['Appeared'].astype(int)
pass1 = df['Group I']['Passed'].astype(int)
passper1 = df['Group I']['Pass %'].astype(float)
appear2 = df['Group II']['Appeared'].astype(int)
pass2 = df['Group II']['Passed'].astype(int)
passper2 = df['Group II']['Pass %'].astype(float)
appearb = df['Both Group']['Appeared'].astype(int)
passb = df['Both Group']['Passed'].astype(int)
passperb = df['Both Group']['Pass %'].astype(float)
data = pd.DataFrame({'appeared' : appear1, 'passed' : pass1}, index = appear1.index)
ax = data.plot(kind = 'bar',figsize = [10,10])
d = 0
bars = ax.patches
for i in range(len(bars)):
    if i < len(bars)/2:
        continue
    ax.text(bars[i].get_x()-.03, bars[i].get_height()+.5, str(passper1.iloc[d])+'%', fontsize=10,color='black')
    d = d + 1
plt.show()
#a.bar(pass1)
plt.show()
data = pd.DataFrame({'appeared' : appear2, 'passed' : pass2}, index = appear1.index)
ax = data.plot(kind = 'bar',figsize = [10,10])
d = 0
bars = ax.patches
for i in range(len(bars)):
    if i < len(bars)/2:
        continue
    ax.text(bars[i].get_x()-.03, bars[i].get_height()+.5, str(passper2.iloc[d])+'%', fontsize=10,color='black')
    d = d + 1
plt.show()
data = pd.DataFrame({'appeared in both' : appearb, 'passed' : passb}, index = appear1.index)
ax = data.plot(kind = 'bar',figsize = [10,10])
d = 0
bars = ax.patches
for i in range(len(bars)):
    if i < len(bars)/2:
        continue
    ax.text(bars[i].get_x()-.03, bars[i].get_height()+.5, str(passperb.iloc[d])+'%', fontsize=10,color='black')
    d = d + 1
plt.show()


