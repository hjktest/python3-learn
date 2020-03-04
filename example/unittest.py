#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: unittest.py
@time: 2020/3/3 20:31
"""
import unittest
from example import mydict
from mydict import Dict
class TestDict(unittest.TestCase):
    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d, dict))


