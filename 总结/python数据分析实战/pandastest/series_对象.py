# coding:utf-8
import pandas as pd
import numpy as np

'''核心两个数据结构
series   ： 索引index 和value，类似一维数据结构，由两个相互关联的数组组成
dataframe ： '''

# 不指定标签，和数组一样
s = pd.Series([12,-4,7,9])
# print("index  value")
# print(s)

# 1为了有意义，在调用构造函数时，制定index 把存放有标签的数组赋给他，标签类型为字符串
n = pd.Series([12,-4,7,9] ,index = ['a','b','c','d'])
# print(n)
#分别查看series的两个数组
# print(n.values)
# print(n.index)

# 2选择元素和修改和数组一样
# print(s[2],n[3])
# print(n['b'])
# print(s[0:2])
# print(n[['b','c']])

# 3赋值
# s[1] = 0
# n['b'] = 1
# print(s,n)

# 4利用numpy 数组或者其他series 对象定义新的series对象.这样做的时候不要忘记
# 新的series对象中的元素不是元numpy的数组或者series对象的副本而是对它的引用，这些对象都是动态的插入到新的series对象中
#如果原有的对象的值发生改变，新的series对象的值也会发生改变
# arr = np.array([1,2,3,4])
# s3 = pd.Series(arr)
# print(s3)
# s = pd.Series([12,-4,7,9])
# s4 = pd.Series(s)
# print(s4)

# 5 筛选元素
# print([s>8])
# print(s[s>8])
# 6 series 对象运算和数学运算
# print(s/2)
# print(np.log(s))

# 7 series 对象组成的元素。生命重复对象
# serd = pd.Series([1,0,2,1,2,3],index=['white','white','blue','green','green','yello'])
# print(serd)
#弄清包含多少个元素
#print(serd.unique())
# 另外一个统计值出现的次数的函数
# print(serd.value_counts())
# isin 判断所属关系
# print(serd.isin([0,3]))
# print(serd.isin([0,3]))
# 8 NaN 数据结构中字段为空或者不符合数字的定义时，用这个特定的值表示
# s2 = pd.Series([5,-3,np.NaN,14])
# print(s2)
'''isnull() 和 notnull() 识别没有对应元素的索引时非常好用'''
# print(s2.isnull())
# print(s2.notnull())

# 9 series 作为字典，用先定义好的字典来创建series对象
# mydict = {'red':2000,'blue':1000,'yello':500,'orange':1000}
# myseries = pd.Series(mdict)
# print(myseries)
# colors = ['red','yello','orange','blue','green']
# myseries = pd.Series(mydict,index=colors)
# print(myseries)
# 10 series 对象之间的运算
# mydict2 = {'red':200,'yello':1000,'black':700}
# myseries2 = pd.Series(mydict2)
# print(myseries+myseries2)

mser = pd.Series(np.random.rand(8),index=[['white','white','white','blue','blue','red','red','red'],['up','down','right'
    ,'up','down','up','down','left']])
print(mser)
print('@'*20)
print(mser.index)