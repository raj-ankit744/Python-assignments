# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 12:30:25 2018

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
X = np.array([[5,3],  
     [10,15],
     [15,12],
     [24,10],
     [30,45],
     [85,70],
     [71,80],
     [60,78],
     [55,52],
     [80,91],])
plt.scatter(X[:,0],X[:,1], label = 'True Position')
plt.show()
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
print(kmeans.cluster_centers_)
print(kmeans.labels_)
plt.scatter(X[:,0],X[:,1],c=kmeans.labels_, cmap = 'rainbow')
plt.show() 
print(kmeans.inertia_)