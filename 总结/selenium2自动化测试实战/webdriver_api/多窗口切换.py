# coding=utf-8
# cding=utf-8

from selenium import webdriver
#from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle
driver.find_element_by_link_text('登陆').click()
driver.find_element_by_link_text('立即注册').click()

# 获得当前所打开的窗口的句柄
all_handles = driver.window_handles

# 进入注册窗口

for handle in all_handles:
    if handle !=sreach_windows:
        driver.switch_to.window(handle)
        print('now register window')
        driver.find_element_by_name('account').send_keys('user')
        driver.find_element_by_name('passeord').send_keys("passeord")
        time.sleep(2)

# 回到搜素窗口
    for handle in all_handles:
        if handle == sreach_windows:
            driver.switch_to.window(handle)
            print("now seach window")
            driver.find_element_by_id('TANGRAM_PSP_2_closeBtn').click()
            driver.find_element_by_id('kw').send_keys('selenium')
            driver.find_element_by_id('su').click()

'''下面的可以正常运行，上面的有错'''
'''
Author: 虫师
Date: 2016/11/22
Method:
  *  switch_to.window()  切换窗口
  *  current_window_handle 获得当前窗口的句柄
  *  window_handles：返回所有窗口的句柄到当前会话
'''
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click()

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_name("userName").send_keys('yisdfjsifj')
        driver.find_element_by_name('phone').send_keys('13932494466')
        driver.find_element_by_name('password').send_keys('1323546787')
        driver.find_element_by_id('TANGRAM__PSP_3__submit').click()
        time.sleep(2)
        # 操作验证码，获取位置 在点击的瞬间，下面的验证图片上出现需要拖动的位置，获取该位置，然后通过鼠标的拖动效果移动验证图片
        '''验证图片<div class="nocaptcha-slice" style="display: block; width: 60px; height: 60px;
         background-image: url(&quot;/static/nocaptcha/6/519b7755b770972.png&quot;);
          left: 278.5px; top: 0px;"></div>'''
        #driver.close()

# 回到搜索窗口
driver.switch_to.window(sreach_windows)
print('now sreach window!')
driver.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)

driver.quit()
