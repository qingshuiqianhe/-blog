# coding:utf-8
import numpy as np
import sys

a = np.array([1,2,3])
print(type(a))
print(a)

a = np.array([3.3,4.5,1.2,5.7,0.3])
print(a.mean()) # 平均值
print(a.std())# 平均差
A = np.arange(10,19).reshape((3,3))
print(A)
#打印第一行
print(A[0,:])
#打印第一列
print(A[:,0])
print("*"*10)
print(A[0:2])
print("*"*10)
print(A[0:2,0:2])
print("*"*10)
print(A[[0,2],0:2])
print("*"*10)
print(A[0,2])

# 转置 A.transpose()

a = np.random.random(12)
a = a.reshape(3,4)
print(a)
print("*"*50)
print(a.transpose())

# 入栈操作  vstack() 执行垂直入栈操作,hstack() 水平入栈操作，column_stack()和row_stack()  把一维数组作为列或行压入栈结构

A = np.ones((3,3))
B = np.zeros((3,3))

C= np.vstack((A,B))
print(C)
print("*"*10)
print(np.hstack((A,B)))
print("*"*10)
a = np.array([0,1,2])
b = np.array([3,4,5])
c = np.array([6,7,8])

print(np.column_stack((a,b,c)))
print("*"*10)
print(np.row_stack((a,b,c)))

# 数组的切分
a = np.arange(16).reshape(4,4)
print(a)
# 水平切分，把数组按照宽度切分成两部分      例如4*4 的切分成两个4*2
[b,c] = np.hsplit(a,2)
print("b:\n",b)
print("*"*25)
print("c:\n",c)
print("*"*20)
# 垂直切分
[e,f] = np.hsplit(a,2)
print('e:\n',e)
print("*"*20)
print('f:\n',f)


# split() 函数，axis =1 索引为列索引，axis = 0 ，索引为行索引

[a1,a2,a3] = np.split(a,[1,3],axis =1)

print("a1:\n",a1)

print("a2；\n",a2)

print("a3:\n",a3)


[b1,b2,b3] = np.split(a,[1,3],axis =0)

print("b1:\n",b1)

print("b2；\n",b2)

print("b3:\n",b3)


# save() 方法以二进制格式保存数据，load()方法从二进制文件中读取数据,格式.npy

print('a\n',a)

saved_data = np.save('saved_data',a)

# 此处load 的用法换了，需要田间mmap_mode = 'r',百度参考文档

loaded_data = np.load('saved_data.npy',mmap_mode='r')

print(loaded_data)



# genfromtxt() 可以从文本文件中读取数据并将其插入数组中，函数接受三个参数，文件名，用于分割的字符，是否含有列标题

# data = np.gemfromtxt('data.csv',delimiter=',',names = True)
#
# print(data)

# 函数包含两层 隐式循环，第一层循环每次读取一行，第二曾循环将第一行的多个值分开后，在对着这些值进行转化，依次插入所创建的元素。
# 函数优点可以处理数据缺失的元素










