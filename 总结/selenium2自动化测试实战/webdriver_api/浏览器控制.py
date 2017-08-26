# coding:utf-8
'''控制浏览器大小'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("www.baidu.com")
print("浏览器宽480，高600")
driver.set_window_size(480,600)



# 控制浏览器的前进和后退
first_url = 'http://www.baidu.com'
driver.get(first_url)
second_url = 'http://www.sina.com'
driver.get(second_url)

# 后退到百度
driver.back()
# 前进到新浪
driver.forward()

# 模拟浏览器的刷新
driver.refresh()