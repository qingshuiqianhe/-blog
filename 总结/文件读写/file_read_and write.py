#!/usr/bin/python
# coding: utf-8

#通过len(file.readlines())来返回一个文件的行数

#通常我们在读取文件的时候，会用到read(), readline(), readlines()
#read(),readlines(),将数据全部读入内存，readlines（）是创建一个列表，read（）读取整个文件
#通常的用法
#1.read()
def test1():
    with open('123.txt', "r") as f:
        print (f.read())
        print(len(f.splitlines()))#打印总行数
    f.close()
#2.readlines()
def test2():
    f = open("123.txt", "r")
    for lines in f.readlines():
        lines = lines.strip('\n')  #python按行读取文件，如何去掉换行符"\n"
        print (lines,end="")    #去掉换行符方法2，加上“,end="" ”
        print(lines)
    f.close()

#python读取大文件的方法
#方法1：
#将文件切分成小段，每次处理完小段内容后，释放内存
#这里会使用yield生成自定义可迭代对象， 即generator， 每一个带有yield的函数就是一个generator

def read_in_block(file_path):
    BLOCK_SIZE = 1024
    with open(file_path, "r") as f:
        while True:
            block = f.read(BLOCK_SIZE)  # 每次读取固定长度到内存缓冲区
            if block:
                yield block
            else:
                return  # 如果读取到文件末尾，则退出

def test3():
    file_path = "123.txt"
    for block in read_in_block(file_path):
        print (block)

#方法2：  一劳永逸
#利用open("", "")系统自带方法生成迭代对象
#for line in f这种用法是把文件对象f当作迭代对象,系统将自动处理IO缓冲和内存管理, 这种方法是更加pythonic的方法,比较简洁
def test4():
    with open('123.txt') as f:
        for line in f:
            line = line.strip('\n')
            print (line)

if __name__ == '__main__':
    test4()


# 按行读取文件，在换行符处进行切片，换行读取下一行
#f = open("123.txt","r")
# f = f.read()
# print(f)
# print(len(f.splitlines()))

#readlines 列表['everthing\n', 'noe \n', 'a\n', 'fire \n', 'fox\n', 'is\n', 'google\n', '[o[\n', '[\n', 'pop']
# f = f.readlines()
# print(f)
# for i in range(0,len(f)):
#     print(f[i],end="")

#一劳永逸
# for line in f:
#     line =line.strip("\n")
#     print(line)

# 块读取文件
# def read_in_block(file_path):
#     block_size = 200
#     with open(file_path,"r") as f:
#         while True:
#             block = f.read(block_size)
#             if block:
#                 yield block
#             else:
#                 return
# def test():
#     file_path = "123.txt"
#     for block in read_in_block(file_path):
#         print(block)
# test()



'''对xlsx的操作创建到写入数据'''
# import requests
# import datetime
# from openpyxl import Workbook
# from openpyxl import load_workbook
# wb = Workbook()
# # 激活 worksheet
# ws = wb.active
# # 数据可以直接分配到单元格中
# ws['A1'] = 42
# # 可以附加行，从第一列开始附加
# ws.append([1, 2, 3])
# # Python 类型会被自动转换
#
# ws['A3'] = datetime.datetime.now().strftime("%Y-%m-%d")
# # 保存文件
# wb.save("12.xlsx")

'''
Python Tutorial (http://www.python.org/doc/current/tut/tut.html) 讨论了
文件的读取和写入，包括如何将一个文件一次一行地读到 list 中
(http://www.python.org/doc/current/tut/node9.html#SECTION0092100
00000000000000)。
• eff-bot (http://www.effbot.org/guides/) 讨论了各种各样读取文件方法
(http://www.effbot.org/guides/readline-performance.htm) 的效率和性能。

• Python Knowledge Base (http://www.faqts.com/knowledge-
base/index.phtml/fid/199/) 回答了关于文件的常见问题
(http://www.faqts.com/knowledge-base/index.phtml/fid/552)。

• Python Library Reference (http://www.python.org/doc/current/lib/) 总结
了所有文件对象模块 (http://www.python.org/doc/current/lib/bltin-file-
objects.html)。'''
