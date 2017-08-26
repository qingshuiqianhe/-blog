# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("HTTP://www.baidu.com")

#输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
time.sleep(1)
# 删除多输入的m
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
time.sleep(1)
# 输入空格+“教程”
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
time.sleep(1)
driver.find_element_by_id('kw').send_keys('教程')
time.sleep(1)
# ctrl+a 全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(1)
# ctrl+ x 剪切输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
time.sleep(1)
# ctrl+ v 复制输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'V')
time.sleep(1)
# 回车键替代单机操作
driver.find_element_by_id('su').send_keys(Keys.ENTER)
time.sleep(1)