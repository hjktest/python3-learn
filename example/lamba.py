#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: lamba.py
@time: 2020/2/26 15:57
"""
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
# print(is_odd(5))
L=list(filter(lambda n:n%2==1, range(1, 20)))
print(L)
def now():
    print("2020年2月26日")

