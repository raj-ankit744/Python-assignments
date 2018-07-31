# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 17:11:09 2018

@author: user
"""

import matplotlib.pyplot as plt
vehicletype = ['Cars', 'Motorbikes', 'Vans', 'Buses']
number = [140, 70, 55 , 5]
colors = ['r', 'b', 'g', 'y']
plt.pie(number, labels = vehicletype, colors = colors, startangle = 90, autopct = '%.1f%%')
plt.show()

