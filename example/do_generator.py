#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: do_generator.py
@time: 2020/2/25 15:31
"""
s=(x*x for x in range(5))
print(s)
for x in s:
    print(x)
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
f=fib(10)
print('fib(10:',f)
for x in f:
    print(x)

#call generator manuanly
g=fib(5)
while 1:
    try:
        x=next(g)
        print('g',x)
    except StopIteration as e:
        print("gennnartor return value:",e.value)
        break
