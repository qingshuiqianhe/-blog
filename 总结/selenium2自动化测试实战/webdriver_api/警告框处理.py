# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 鼠标悬停在 设置 链接
driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()


# 打开搜索设置
driver.find_element_by_link_text('搜索设置').click()

# 保存设置
driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)

# 接受警告框
driver.switch_to_alert()

'''switch_to_alert()可以定位到alert/confirm/prompt，然后使用text/accept/dismiss/send_keys 处理
test： 返回alert/confirm/prompt 的文字信息
accept： 接受现有警告框
dismiss ： 解散现有警告框
森达——keys（keystosend）： 发送文本至警告框'''