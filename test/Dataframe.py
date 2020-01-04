#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: Dataframe.py
@time: 2020/1/4 16:09
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
ts = pd.Series(np.random.randn(1000),
index=pd.date_range('1/1/2000', periods=1000))
ts = pd.Series(np.random.randn(1000),
index=pd.date_range('1/1/2019', periods=1000))
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
print(plt.figure())
print(df.plot())
plt.legend(loc='best')
plt.show()