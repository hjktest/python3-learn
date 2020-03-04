#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: key param.py
@time: 2020/3/4 20:08
*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。
"""
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

print(person('Mciheal',30))
# 也可以传入任意个数的关键字参数：
print(person('Bob',35,city='Beijing'))
print(person('Adam', 45, gender='M', job='Engineer'))
# 关键字参数有什么用？它可以扩展函数的功能。
# 比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra={'city':'beijing','job':'Engineer'}
print(person('jack',24,city=extra['city'],job=extra['job']))
print(person('jack',24,**extra))
# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
# 仍以person()函数为例，我们希望检查是否有city和job参数：
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job'in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
    # 但是调用者仍可以传入不受限制的关键字参数：
print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name,age,*,city,job):
    print(name,age,city,job)
    # 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
print(person('Jack', 24, city='Beijing', job='Engineer'))
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name,age,*args,city,job):
    print(name,age,args,city,job)
# print(person('Jack', 24, 'Beijing', 'Engineer'))
# 由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。

# 命名关键字参数可以有缺省值，从而简化调用
def person(name,age,*,city='Beijing',job):
    print(name,age,city,job)

print(person('jack',24,job='Engineer'))
# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 比如定义一个函数，包含上述若干种参数：
def f1(a,b,c=0,*args,**kw):
    print('a=', a, 'b=', b,'c=', c,'args=', args,'kw=', kw)
def f2(a,b,c=0,*,d,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
print(f1(1,2))
print(f1(1,2,c=3))
print(f1(1, 2, 3,5,6, 'a', 'b'))
print( f1(1, 2, 3, 'a', 'b','dfdfgdsf',x=99,y='nihao',age=56))
print(f2(1, 2, d=99, ext=None))
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print(f1(*args,**kw))
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args,**kw))