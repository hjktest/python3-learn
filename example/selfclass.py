#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: selfclass.py
@time: 2020/3/3 17:05
"""
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    # __repr__=__str__
print(Student('Michael'))
s=Student('John')
print(s)

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>10000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)

class Fib1(object):
    def __getitem__(self, n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
f=Fib1()
print(f[5])
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n,int):#n是索引
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
                start=n.start
                stop=n.stop
                if start is None:
                    start=0
                a,b=1,1
                L=[]
                for x in range(stop):
                    if x>=start:
                        L.append(a)
                    a,b=b,a+b
                return L
f1=Fib2()
print(f1[0:5])
print(f1[:10])
print(f1[:10:2])