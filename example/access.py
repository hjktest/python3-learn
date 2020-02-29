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
# if.self.name update:self__name,self.__score但是已经无法从外部访问实例变量.__name和实例变量.__score了：
    def get_name(self):
        return self.name
    def get_score(self):
        return self.score

    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'
bart=Student('Bart simpson',59)
print('bart.get_name()=',bart.get_name())
bart.set_score(60)
print('bart.get_score()=',bart.get_score())
print('Do Not user bart.Student_name:',bart.__Student_name)