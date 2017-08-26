import sys
#sys.path.append("F:/Sublime Text 3/Sublime Text 3/手动案例/总结/多重目录调用/model")
sys.path.append("./model")

'''修改1：在new_count 采用.count 引用时，test 正常
   修改2：添加路径引入import sys  和添加路径，相对或者绝对好像没关系'''
from model import new_count
test = new_count.B()
test.add(2,5)