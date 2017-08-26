#coding:utf-8
from selenium import webdriver
import os

fp = webdriver.FirefoxProfile()
#  0 默认路径   2指定目录
fp.set_preference("browser.download.folderList",2)
# 是否显示开始 True 显示
fp.set_preference("browser.download.manager.showWhenStarting",False)
# 用于指定所下载的文化目录。os.getcwd()不需要参数，用于返回当前目录
fp.set_preference("browser.download.dir",os.getcwd())
#
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")# 下载文件类型

driver = webdriver.Firefox(firefox_profile=fp)
driver.get('http://pypi.python.org/pypi/selenium')
driver.find_element_by_partial_link_text('selenium-2').click()