# coding:utf-8
'''1 调用滚动条'''
from selenium import webdriver
from time import sleep

# 访问百度
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 控制浏览器大小
driver.set_window_size(600,600)

# 搜索
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

# 通过javascript 设置浏览器窗口滚动条位置
js = "window.scrollTo(100,450);"
driver.execute_script(js)
sleep(3)


'''向页面中的textarea 文本输入框添加内容'''
text = 'input text'
js = "var sum =document.getElementById('id');sum.value='" + text + "';"
driver.execute_script(js)