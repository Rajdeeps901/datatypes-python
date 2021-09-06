# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 18:37:49 2021

@author: Sing
"""

print("Hellow world")
#LIST
lis=[1,2,3,4,5,6]
print(lis)
print(lis[3:])
print(lis[:4])
lis[2]="9"
print(lis)
len(lis)

#string
str1='hi,i am rajdeep'
str2='how are you'
print(str1*2)
print(str1+str2)
print(str1[2:])

#tuple
t=('a','b','c','d','e','f','g')
print(t)
print(t*2)
print(t[2:])

t[2]="k"
print(t)
print(type(t))

#dictionary
dic={'1':'abc','2':'def','3':'ghi'}
print(dic)
print(dic.keys())
print(dic.values())
print(+dic[1])

#set
set1={1,2,3,4,5,6,7,7,7}
print(set1)
abc=set([1,2,3,4,5,6])
print(abc)
'8'in set1



