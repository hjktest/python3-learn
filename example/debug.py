#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: debug.py
@time: 2020/3/3 20:06
"""
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:',e)
    finally:
        print("finally..")

try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')