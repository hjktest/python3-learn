#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: moreThread.py
@time: 2020/3/6 17:53
"""
import time,threading
def loop():
    print('thread %s is running ...' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('threading %s ended.' % threading.current_thread().name)

print('thread %s is running ...' % threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join(
print('thread %s ended.' % threading.current_thread().name)
)

