#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: Plotting.py
@time: 2020/1/4 15:57
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Series
ts = pd.Series(np.random.randn(1000),
index=pd.date_range('1/1/2000', periods=1000))
ts = pd.Series(np.random.randn(1000),
index=pd.date_range('1/1/2019', periods=1000))
ts = ts.cumsum()
ts.plot()

plt.show()
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure()