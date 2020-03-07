#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: use_hashlib.py
@time: 2020/3/7 15:38
"""
import hashlib
md5=hashlib.md5()
md5.update('how to user md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1=hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())