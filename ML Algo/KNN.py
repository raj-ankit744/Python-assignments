# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 09:12:23 2018

@author: user
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
df = pd.read_csv('iris.csv')
from sklearn.preprocessing import LabelEncoder
#print(df.columns)
x = df.iloc[:,0:-1].astype(float)
y = df.iloc[:,-1]
#print(y)
l = LabelEncoder()
l.fit(y)
y = l.transform(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
C = KNeighborsClassifier(n_neighbors = 10)
model = C.fit(x_train, y_train)
y_pred = C.predict(x_test)
plt.scatter(x_test.iloc[:,1], y_pred,color = 'r')
print(model.score(x_test, y_test))