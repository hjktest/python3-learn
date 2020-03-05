#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: StringIOandBytesIO.py
@time: 2020/3/5 16:51
"""
from io import StringIO
from io import BytesIO
f=StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())

f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())