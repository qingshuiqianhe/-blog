'''列表的操作总结'''

#1，全数字列表进行排列 1.sort() 由小到大 2.reverse()，倒序排列 3.sorted 创建列表副本进行有大到小排序
a = [3,2,1]
a.sort()    #sort 对列表元素进行排列
max = a[len(a)-1]
min = a[0]
a.reverse()
c = sorted(a)
print(c)

# 2添加元素  1：append，在最后一个位置添加，2：extend：逐个添加列表c的元素加入列表a末尾，3.indsert（i,num ）  在制定位置添加某个元素
a=[]
for i in range(10,1,-1):
    a.append(i)
    print(a)    # [10, 9, 8, 7, 6, 5, 4, 3, 2]
c = ['c','d','e']
a.extend(c) # 将列表c 元素逐个添加到列表a 的末尾,[10, 9, 8, 7, 6, 5, 4, 3, 2, 'c', 'd', 'e']
print(a)
a.insert(2,16)
print(a)    #[10, 9, 16, 8, 7, 6, 5, 4, 3, 2, 'c', 'd', 'e']

# 3对列表进行操作时注意为了保留原来列表数据，采用新建列表副本，对副本进行操作，以免数据的丢失
new_list = a[:]
new_list.append("sss")  #[10, 9, 8, 7, 6, 5, 4, 3, 2, 'c', 'd', 'e', 'sss']
print(new_list)
print(a)    #[10, 9, 8, 7, 6, 5, 4, 3, 2, 'c', 'd', 'e']

# 4 修改元素值
#确定元素的位置，对其重新赋值即可
a[0]=100
print(a)    #[100, 9, 8, 7, 6, 5, 4, 3, 2, 'c', 'd', 'e']

#5删除元素  1.del a[num] 删除指定位置元素 2. a.pop()删除末尾元素 3.remove("") 删除列表内的指定名字的元素
del new_list[0]
new_list.pop()
new_list.remove(16)
print(new_list)

# 6 查找元素 1.in bool 表达式，在返回true，不在返回false 2.查找索引，index（‘c’），返回c的下标
if 'a' in new_list:
    print(True)
else:
    print(False)
print(new_list.index('c'))


#列表嵌套
b = ['a','s','d']
d = ['q','w','e','r']
new_list.append(b)
new_list.append(d)
#打印列表 b中的  第二个元素
print(new_list[11][1])



# 字典操作中，键值对自动添加问题
# a={"name":"123","sex":"dd"}
# a["id"]="45456"
# print(a)