# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:11:34 2018

@author: user
"""
from sortedcontainers import SortedSet
import random, math, numpy as np
def dist(x,y):
    return math.sqrt((x[1]-x[0])**2 + (y[1]-y[0])**2)

x = [5,10,15,24,30,85,71,60,55,80]
y = [3,15,12,10,45,70,80,78,52,91]
k = 2
c = []
s = SortedSet()
cen = dict()
cn = dict()
#for i in range(k):
#    c.append(random.randint(0,6))


c = [0,1]
print(c)
for i in c:
    cn[i] = set([(x[i],y[i])])
    cen[i] =(x[i],y[i])
for i in range(4):
    vis = set([i for i in range(len(x))])
    meanx = []
    meany = []
    cn.clear()
    while len(vis) != 0:
        for cx in cen.keys():
            if len(vis) == 0:
                continue
            for j in vis:
                s.add((dist((list(cen[cx])[0],x[j]),(list(cen[cx])[1],y[j])), j, cx))
        l = s.pop(0)
        while(l[1] not in vis):
            l = s.pop(0)
        vis.remove(l[1])
        if l[2] not in cn.keys():
            cn[l[2]] = set()
        cn[l[2]].add((x[l[1]],y[l[1]]))
    print(cn)
    for k in cn.keys():
        meanx.append(np.mean([i[0] for i in cn[k]]))
        meany.append(np.mean([i[1] for i in cn[k]]))
    cnt = 0
    for k in cen.keys():
        cen[k] = (meanx[cnt],meany[cnt])
        cnt = cnt + 1
    print(cen)
    
