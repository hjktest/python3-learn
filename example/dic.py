#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: dic.py
@time: 2020/2/22 12:00
"""
d={
    'Michael':95,
    'Bob':75,
    'tracy':85

}
print('d[\'Michael\']=',d['Michael'])

def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(pow(5,3))
# //我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
numbers=(1,2,3,4,5,6,7,8,9,10)
print(calc(numbers))

def person(name, age, *, city, job):
    print(name, age, city, job)

print(person('Jack', 24, city='Beijing', job='Engineer'))
