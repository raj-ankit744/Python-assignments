# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:56:44 2018

@author: user
"""
from sklearn.linear_model import LinearRegression
import pandas as pd,numpy as np
dataset = pd.read_csv("C:/Users/user/Desktop/ARG/week 2 ex 2/headbrain.csv")
x = dataset['Head Size(cm^3)'].values.reshape(-1,1)
y = dataset['Brain Weight(grams)'].values.reshape(-1,1)
regressor = LinearRegression()  
regressor.fit(x,y)
print(regressor.intercept_)
print(regressor.coef_)
y_pred = regressor.predict(x)
from sklearn import metrics  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y, y_pred)))
print('R2: ', metrics.r2_score(y,y_pred))