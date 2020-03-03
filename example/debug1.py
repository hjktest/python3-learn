#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: debug1.py
@time: 2020/3/3 20:17
"""
import logging
logging.basicConfig(level=logging.INFO)
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

s='0'
n=int(s)
logging.info('n=%d' %n)
print(10 / n)