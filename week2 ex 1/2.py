# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:52:08 2018

@author: user
"""


import matplotlib.pyplot as plt
vehicletype = ['Beast Animals', 'Other Land Animals', 'Birds', 'Water Animals', 'Reptiles']
number = [150, 400, 225 , 175, 50]
colors = ['r', 'b', 'g', 'y', 'c']
plt.pie(number, labels = vehicletype, colors = colors, startangle = 90, autopct = '%.1f%%')
plt.show()

