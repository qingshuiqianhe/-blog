# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.126.com")

# 打印当前页面和url
print(driver.title)
print(driver.current_url)

# 执行邮箱登陆
'''网易邮箱的id是现在随机换了。而且xpath也不一定可以匹配的到，应该是上层的class没有变，结合下面的信息进行匹配应该可以
等可以总结的时候在回来弄网易邮箱'''
driver.find_element_by_id("auto-id-1501147907149").clear()
driver.find_element_by_css_name('u-label f-dn').send_keys('username')
driver.find_element_by_id("auto-id-1501147796727").clear()
driver.find_element_by_id("auto-id-1501147796727").send_keys("password")
driver.find_element_by_id('dologin').click()
'''126邮箱登陆'''

# 打印当前页面和url
print(driver.title)
print(driver.current_url)

# 获取当前用户名
user = driver.find_element_by_id("spenUid").text
print(user)