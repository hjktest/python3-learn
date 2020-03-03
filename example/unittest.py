#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: unittest.py
@time: 2020/3/3 20:31
"""
class Dict(dict):
    def __int__(self,**kw):
        super.__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise  AttributeError("DIc object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key]=value

