#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: multiprocessing.py
@time: 2020/3/6 18:22
"""
import threading,multiprocessing

def loop():
    x = 0
    while True:
        x = x^1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()