#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: urllib_exam.py
@time: 2020/3/7 16:20
"""
from urllib import  request

with request.urlopen('https://www.baidu.com') as f:
    data=f.read()
    print("Status:",f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' %(k,v))
    print('Data:',data.decode('utf-8'))