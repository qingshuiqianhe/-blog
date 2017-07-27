from count import A
class B(A):
	def sub(self,a,b):
		return a-b
resule = B().add(2,5)
print(resule)


'''方法1,   .count  修改为如下代码    引入后test不用变，但本身new_count 报错
错误信息：
Traceback (most recent call last):
  File "F:/Sublime Text 3/Sublime Text 3/手动案例/总结/多重目录调用/model/new_count.py", line 10, in <module>
    from .count import A
ModuleNotFoundError: No module named '__main__.count'; '__main__' is not a package

创建了两个名字的空文件，放在哪个目录页都报错，还有书上的__init__.py,都创建了，但也不行'''
# from count import A
# class B(A):
# 	def sub(self,a,b):
# 		return a-b
# resule = B().add(2,5)
# print(resule)