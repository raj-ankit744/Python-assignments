# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:19:37 2018

@author: user
"""
import operator
n = []
for i in range(10):
    n.append(input("Enter name marks1 marks2 marks3").split())
for i in range(10):
    print(n[i][0]+ " "+ n[i][1] + " " + n[i][2] + " " + n[i][3])
    
s1 = []
s2 = []
s3 = []
    
for i in range(10):
    s1.append(int(n[i][1]))
    s2.append(int(n[i][2]))
    s3.append(int(n[i][3]))
s1.sort()
s2.sort()
s3.sort()

print("Subjectwise mean : ", sum(s1)/10, sum(s2)/10, sum(s3)/10)
print("Subjectwise median: ",(s1[4] + s1[5])/2, (s2[4] + s2[5])/2, (s3[4] + s3[5])/2)
print("Sub1")
for i in range(10):
    print(s1[i])
print("Sub2")
for i in range(10):
    print(s2[i])
print("Sub3")
for i in range(10):
    print(s3[i])

st = []
for i in range(10):
    st.append((int(n[i][1]) + int(n[i][2]) + int(n[i][3]),n[i][0]))
st.sort(reverse=True)
print("Top 3 students : ")
print(st[0])
print(st[1])
print(st[2])

for i in range(10):
    if st[i][0]/3 > 90:
        print(st[i][1] + ":A+")
    elif st[i][0]/3 > 80:
        print(st[i][1] + ":A")
    elif st[i][0]/3 > 70:
        print(st[i][1] + ":B+")
    elif st[i][0]/3 > 60:
        print(st[i][1] + ":B")
    elif st[i][0]/3 > 50:
        print(st[i][1] + ":C")
    else:
        print(st[i][1] + ":D")
        