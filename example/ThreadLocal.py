#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: ThreadLocal.py
@time: 2020/3/6 19:47
"""
import  threading
#创建全局变量threadlocal
local_school=threading.local()
def process_student():
    # 获取当前线程关联的student
    std=local_school.student
    print('Hello,%s (in %s)' % (std,threading.current_thread().name))
def process_thread(name):
    # 绑定threadlocal的student
    local_school.student=name
    process_student()
t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread_a')
t2=threading.Thread(target=process_thread,args=('Bob',),name='Thread_b')
t1.start()
t2.start()
t1.join()
t2.join()