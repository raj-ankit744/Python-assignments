# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 17:22:10 2018

@author: user
"""
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
X = np.array([14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1])
Y = np.array([215, 325, 185, 332, 406, 522, 412, 614])
plt.scatter(X, Y)
X = X.reshape(-1,1)
Y = Y.reshape(-1,1)
lm = LinearRegression()
lm.fit(X,Y)
Y_pred = lm.predict(X)
plt.plot(X,Y_pred)
plt.show()
