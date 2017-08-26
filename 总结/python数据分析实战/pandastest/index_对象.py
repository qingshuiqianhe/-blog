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
print('*'*30)
frame['price'][2] = 3.3
print(frame)