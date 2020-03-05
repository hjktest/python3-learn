#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: file_write_read.py
@time: 2020/3/5 16:13
"""
from datetime import datetime
f = open('c:\\qq_test1.txt', 'r')
# print(f.read())

with open('C:\\selenium\\data\\password.txt','r',encoding='gbk') as f:
    print(f.read())

with open('C:\\selenium\\data\\password.txt','a') as f:
    f.write('Hello world!')
with open('C:\\selenium\\data\\password.txt','r',encoding='gbk') as f:
    print(f.read())

with open('test.txt', 'w',encoding='utf-8') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r',encoding='UTF-8') as f:
    s = f.read()
    print('open for read...')
    print(s)
with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)