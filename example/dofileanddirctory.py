#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: dofileanddirctory.py
@time: 2020/3/5 17:04
"""
import os
print(os.name)
# linux exist
# print(os.uname)
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用
print(os.path.abspath('.'))
# 创建新目录
os.path.join('C:\\selenium','testdir')
# print(os.mkdir('C:\\selenium\\testdir'))
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])