#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: Itertools.py
@time: 2020/3/7 15:59
"""
import itertools
# natuals=itertools.count(1)
# for n in natuals:
#     print(n)
# cs=itertools.cycle('ABC')
# for c in cs:
#     print(c)
ns=itertools.repeat('A',3)
for n in ns:
    print(n)
natuals=itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,natuals)
print(list(ns))
for c in itertools.chain('ABC', 'XYZ'):
    print(c)
for key,group in itertools.groupby('AAABBBCCAAA'):
    print(key,list(group))
for key,group in itertools.groupby('AaaBBcAAa',lambda c : c.upper()):
    print(key,list(group))