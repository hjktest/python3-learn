#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: access.py
@time: 2020/2/29 14:32
"""
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def get_name(self):
        return self._name
    def get_score(self):
        return self._score

    def set_score(self,score):
        if 0<=score<=100:
            self._score=score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self._score>=90:
            return 'A'
        elif self._score>=60:
            return 'B'
        else:
            return 'C'
bart=Student('Bart simpson',59)
print('bart.get_name()=',bart.get_name())
bart.set_score(60)
print('bart.get_score()=',bart.get_score())
print('Do Not user bart.Student_name:',bart._Student_name)