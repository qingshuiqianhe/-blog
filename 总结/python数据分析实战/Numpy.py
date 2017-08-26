# coding:utf-8
import numpy as np
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









