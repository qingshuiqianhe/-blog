# coding:utf-8
'''1.send_keys 指定本地文件路径上传,避免了操作windows 控件的步骤，
找到上传的input标签，通过send_keys 输入文件地址实现上传'''
from selenium import webdriver
import os

driver = webdriver.Chrome()
file_path = 'file:///' +os.path.abspath('upfile.html')
driver.get(file_path)
#定位上传按钮，添加本地文件
driver.find_element_by_name('file').send_keys('D:\\uplaod_file.txt')

driver.quit()

'''2 Autolt  自行下载体验，生成exe供python 调用'''
from  selenium import webdriver
import os

# 打开上传功能的页面
driver= webdriver.Chrome()
driver.get(file_path)

# 单击打开上传窗口
driver.find_element_by_name('file').click()
# 调用exe
os.system("D:\\upfile.exe")

driver.quit()
