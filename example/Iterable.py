#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: Iterable.py
@time: 2020/2/22 16:54
"""
for x,y in [(1,4),(2,5),(3,6)]:
    print(x,y)

print([x*x for x in range(1,101)])

print([x*x for x in range(1,101) if x%2==0])
print([x*x for x in range(1,101) if x%2==1])
print([x for x in range(1,101) if x%x==1])

d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)

L=['Hello','World','IBM','Apple']
print[s.lower()  for s in L ]
