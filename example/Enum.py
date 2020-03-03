#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: Enum.py
@time: 2020/3/3 17:55
"""
from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

day1=Weekday.Mon
print(day1)
print(day1 == Weekday.Mon)
for name, member in Weekday.__members__.items():
     print(name, '=>', member)
