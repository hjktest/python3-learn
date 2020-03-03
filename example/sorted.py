#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: sorted.py
@time: 2020/2/29 10:25
"""
from operator import itemgetter
L=['bob','about','Zoo','Credit']
print(sorted(L))
print(sorted(L,key=str.lower))
students=[('Bob',75),("Adam",92),("Jone",66),('Lisa',88)]
print(sorted(students,key=itemgetter(0)))
print(sorted(students,key=lambda t:t[1]))
print(sorted(students,key=itemgetter(1),reverse=True))

print(sorted([36, 5, -12, 9, -21]))
# abs
print(sorted([36,5,-12,9,-21],key=abs))
# 我们给sorted传入key函数，即可实现忽略大小写的排序：
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))