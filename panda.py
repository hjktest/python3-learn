# coding:utf-8
#file: panda.py
__author__ = 'Administrator'
#@time: 2020/1/3 13:22
#@desc:
import numpy as np
import pandas as pd
s = pd.Series([1,3,4,np.nan,7,9])
print(s)
print(pd.Series([1,3,4,np.nan,7,9], index=[1,1,2,2,'a',4]))
#新建一个DataFrame对象可以有多种方式
dates = pd.date_range('20190101', periods=6)
print(dates)
#添加列
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
#通过传入一个dict对象
df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20190101'),
                    'C':pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D':np.array([3]*4, dtype='int32'),
                    'E':pd.Categorical(["test", "tain", "test", "train"]),
                    'F':'foo'})

print(df2)
print(df2.dtypes)

# 查看开头几行或者末尾几行：
print(df.head())
print(df.tail(3))

print(df.index)
print(df.columns)
print("**********************************")
print(df.to_numpy())
print(df2.to_numpy())
#查看数据的简要统计结果
print(df.describe())
#转置
print(df.T)
#按坐标轴排序按坐标轴排序，其中axis参数为坐标轴，axis默认为0，即横轴（对行排序），axis=1则为纵轴（对列排序）；
# asceding参数默认为True，即升序排序，ascending=False则为降序排序：
print("**********************************")
print(df.sort_index(axis=1))
print(df.sort_index(axis=1,ascending=False))
#可见df.sort_index(axis=1)是按列名升序排序，所以看起来没有变化，当设置ascending=False时，列顺序变成了DCBA。
# 按数值排序：
print(df.sort_values(by="B"))
print(df.sort_values(by='B', ascending=False))
# 筛选 Selection
# 获取某列
print(df['A'])
# 选择多行
print(df[0:3])
print(df['20190101':'20190104'])
#通过标签选择
print(df.loc[dates[0]])
# 选择指定行列的数据
print(df.loc[:,('A','C')])
print(df.loc['20190102':'20190105', ('A', 'C')])
# 选定某值
print(df.loc['20190102', 'A'])
print(df.at[dates[1], 'A'])
#通过位置选择
print(df.iloc[3])
#选择指定行列的数据
print(df.iloc[3:5, 0:2])
print(df.iloc[:,:])
print(df.iloc[[1, 2, 4], [0, 2]])
# 选择某值
print(df.iloc[:,:])
print(df.iloc[1, 1])
print(df.iat[1, 1])
# 条件判断选择
# 按某列的数值判断选择
print(df[df.A > 0])
# 筛选出符合要求的数据
# 使用isin()方法筛选
df2=df.copy()
df2['E']= ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
print(df2['E'].isin(['two','four']))
print(df2[df2['E'].isin(['two','four'])])
print(df.isin([-1.116207]))
# 设定值
# 通过指定索引设定列
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20190102', periods=6))
print(s1)
df['F']=s1
print(df)
# 通过标签设定值
df.at[dates[0],'A']=0
print(df)
# 通过为止设定值
df.iat[0,1]=0
print(df)
# 通过NumPy array设定值
df.loc[:, 'D'] = np.array([5] * len(df))
print(df)
#通过条件判断设定值
# 空值处理 Missing Data
# 通过reindex()方法可以新增、修改、删除某坐标轴（行或列）的索引，并返回一个数据的拷贝
df1 = df.reindex(index=dates[0:4],columns=list(df.columns)+['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)
# 删除空值
df1.dropna(how='any')
print(df1)
# 填充空值
df1.fillna(value=5)
print(df1)
# 判断是否为空值
print(pd.isna(df1))
# 运算 Operations
print(df.mean())
# 如果需要按行求平均值，需指定轴参数：
print(df.mean(1))
# 数值移动
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates)
print(s)
s = s.shift(2)
print(s)
# 不同维度间的运算，pandas会自动扩展维度：
df.sub(s, axis='index')
print(df)

# 通过apply()方法，可以对数据进行逐一操作:
print(df.apply(np.cumsum))
# 这里使用了apply()方法调用np.cumsum方法，也可直接使用df.cumsum()
print(df.cumsum())
# 统计矩阵中每个元素出现的频次：
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())
# 所有的Series类型都可以直接调用str的属性方法来对每个对象进行操作。
# 比如转换成大写
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.upper())
# pandas`可以提供很多方法可以快速的合并各种类型的Series、DataFrame以及Panel Object。
df = pd.DataFrame(np.random.randn(10, 4))
print(df)
pieces=[df[:3],df[3:7],df[7:]]
print(pieces)
print(pd.concat(pieces))
#这是类似sql的合并方法
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on='key'))
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on='key'))
# Append方法
# 在DataFrame中增加行
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df)
s = df.iloc[3]
print(s)
df.append(s,ignore_index=True)
print(df)
df.append(s)
print(df)
# 分组：选择需要的数据
# 计算：对每个分组进行计算
# 合并：把分组计算的结果合并为一个数据结构中
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                    'foo', 'bar', 'foo', 'foo'],
                    'B': ['one', 'one', 'two', 'three',
                    'two', 'two', 'one', 'three'],
                    'C': np.random.randn(8),
                    'D': np.random.randn(8)})
print(df)
print(df.groupby('A').sum())
print(df.groupby(['A', 'B']).sum())
df2 = df[:4]
print(df2)
# 使用stack()方法，可以通过堆叠的方式将二维数据变成为一维数据：
stacked = df2.stack()
print(stacked)
# 对应的逆操作为unstacked()方法：
print(stacked.unstack())
# 表格转置
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
'B': ['A', 'B', 'C'] * 4,
'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
'D': np.random.randn(12),
'E': np.random.randn(12)})
print(df)
# 通过pivot_table()方法可以很方便的进行行列的转换：
print(pd.pivot_table(df,values='D',index=['A','B'],columns=['C']))
# 时间间隔调整
rng = pd.date_range('1/1/2019', periods=100, freq='h')
print(rng[:5])
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts.head(5))
## 按10s间隔进行重新采样
ts1 = ts.resample('10S')
print(ts1)
## 用求平均的方式进行数据整合
print(ts1.mean())
## 用求和的方式进行数据整合
print(ts1.sum())
# 显示时区：
rng = pd.date_range('1/1/2019 00:00', periods=5, freq='D')
print(rng)
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)
# 关于Categories类型介绍可以参考：http://pandas.pydata.org/pand...
# 类型转换：astype('category')
df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
"raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
print(df)
df['grade']=df['raw_grade'].astype('category')
print(df['grade'])