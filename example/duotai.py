#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: duotai.py
@time: 2020/2/29 16:48
"""
class Animal(object):
    def run(self):
        print('Animal is runing..')
class Dog(Animal):
    def run(self):
        print('Dog is running ...')
class Cat(Animal):
    def run(self):
        print("Cat is running..")
def run_twice(animal):
    animal.run()
    animal.run()
a=Animal();
d=Dog()
c=Cat()
print("A is Aniaml?",isinstance(a,Animal))
print('a is Gog?',isinstance(a,Dog))
print('a is Cat',isinstance(a,Cat))
print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))
run_twice(c)