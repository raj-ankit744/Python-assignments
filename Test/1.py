# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:54:51 2018

@author: user
"""
import collections,re
n = int(input("Enter no. of sentences"))
if n < 4:
    print("Enter atleast 4 sentences")
else:
    l = []
    for i in range(n):
        l.append(input())
    print("\n".join(l))
    
    mid = n//2
    l2 = ["UST global specializes in Healthcare, Retail & Consumer Goods, Banking & Financial Services, Telecom, Media & Technology, Insurance, Transportation & Logistics and Manufacturing & Utilities"]
    l = [l[i] for i in range(mid)] + l2 + [l[i] for i in range(mid,n)]
    print("updated para : ","\n".join(l))
    vow = "AEIOUaeiou"
    spc = "~!@#$%^&*(()_+-=`.,<>/?':;[]{}\|"
    x = " ".join(l)
    v = sum(1 for i in x if i in vow)
    up = sum(1 for i in x if i.isupper())
    lo = sum(1 for i in x if i.islower())
    sp = sum(1 for i in x if i in spc)
    count = dict(collections.Counter((" ".join(l)).split()))
    cnt = []
    for x in count.keys():
        if count[x] > 1:
            cnt.append((x,count[x]))
    print(cnt)
    print("No. of vowels ", v)
    print("no. of uppercase characters ",up)
    print("no. of lowercase characters ",lo)
    print("no. of special characters ",sp)
    l1 = re.sub(r'[^A-Za-z0-9]+',r'',' '.join(l))
    print("Paragraph after removing special characters")
    print(l1)
    l[0], l[n] = l[n], l[0]
    print("\n".join(l))
    