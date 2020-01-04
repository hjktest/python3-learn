#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: shanghaizhishu.py
@time: 2019/11/24 18:02
"""
import tushare as ts
import pandas as pd
# ts.set_token('547d03802f1495c635885802cc129e70b308afed664f86b2f8e0a880')
pro=ts.pro_api('547d03802f1495c635885802cc129e70b308afed664f86b2f8e0a880')

df_daily=pro.index_daily(ts_code="000001.SH")
df_daily.head()


