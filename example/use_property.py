#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: use_property.py
@time: 2020/2/29 19:45
"""
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value >100:
            raise ValueError('score mmust be between 0-100!')
        self._score=value

s=Student()
s.score=60
print('s.score=',s.score)
s.score=9999
