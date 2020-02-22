#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: bmi.py
@time: 2020/2/22 11:36
"""
height = 12.5
weight = 80.5
bmi = (weight/height)*(weight/height)
print(bmi)
if 18.5<bmi<25 :
    pass
    print("正常 ")
elif 25<bmi<30:
     print("过重")
else:
    print("该减肥了！")