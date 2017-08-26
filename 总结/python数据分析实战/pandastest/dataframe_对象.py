# coding:utf-8
import pandas as pd
import numpy as np

'''
类似excel

'''
# 1定义dataframe
data = {'color':['blue','green','yello','red','white'],
            'object':['ball','pen','pencil','paper','mug'],
            'price':[1.2,1.0,0.6,0.9,1.7]}
frame = pd.DataFrame(data)
print(frame)
    # columns  筛选指定的列
frame2 = pd.DataFrame(data,columns=['object','price'])
print(frame2)
    #index 指定索引
frame2 = pd.DataFrame(data,index=['one','two','three','four','five'])
print(frame2)
    # 简单创建方法
frame3 = pd.DataFrame(np.arange(16).reshape(4,4),
                      index=['blue','green','yello','red'],
                      columns=['ball','pen','pencil','paper'])
print(frame3)
# 2 选取元素
    # 想知道dataframe 对象的所有列的名字，在它上面调用columns属性
print(frame.columns)
    # 2.2获取数据结构中的元素，values 属性获取所有元素
print(frame.values)
    # 2.3某一列的名称作为索引,返回值为series 对象
print(frame['price'])
    # 2.4用列名称作为dataframe实例的属性
print(frame.price)
    #2.5至于dataframe中的行，用ix 属性和行的索引即可,
    # 返回的同样是series对象，列名称变为索引数组的标签，列中的元素变为series的数据部分
print(frame.ix[2])
print('*'*20)
print(frame.ix[[2,4]])
    # 2.6从dataframe 中抽取一部分。用索引值选择想要的行
print(frame[0:1])
print('*'*20)
print(frame[1:3])
    # 2.7获取dataframe 中的一个元素，依次指定元素所在的列名称、行的索引值或标签
print(frame['object'][3])

# 3 赋值
    # 3.1用colums 属性指定包含列名称的行，还可以用name属性为这两个二级结构指定标签，便于识别
frame.index.name = 'id'
frame.columns.name = 'item'
print(frame)
    # 3.2增加新的一列
frame['new'] = 12
print(frame)
print('*'*20)
frame['new'] = [3.0,1.3,2.2,0.8,1.1]
print(frame)
    # 3.3如果更新某一列的全部数据，方法类似。例如借助np.arange()函数预先定义一个序列，用它更新某一列的全部元素
    # eg： 生成一个递增序列
ser = pd.Series(np.arange(5))
print(ser)
frame['new'] = ser
print(frame)
    # 3.4修改单个元素
# frame['price'][2] = 3.3
# print(frame)

# 4 元素的所属关系
frame4 = frame.isin([1.0,'pen'])
print(frame4)
print(frame[frame.isin([1.0,'pen'])])

# 5删除一列
del frame['new']
print(frame)

# 6 筛选
print(frame[frame <10])
# 7 嵌套字典生成dataframe 对象
nestdict = {'red':{2012:22,2013:33},
            'white':{2011:13,2012:22,2013:16},
            'blue':{2011:17,2012:27,2013:18}}
frame5 = pd.DataFrame(nestdict)
print(frame5)
# 8 转置
print(frame5.T)
