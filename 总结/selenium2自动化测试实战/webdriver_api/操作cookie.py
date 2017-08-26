# coding:utf-8
'''
webdriver 操作cookie的方法
get_cookes(): 获取所有的cookies信息
get_cookie(name) : 返回字典的key为’name‘的cook信息
add_cookie(cookie_dict) : 添加cookie。“cookie_dict”指定字典对象，必须有name 和value的值
delete_cookie(name,optionsString): 删除cookie 信息name为名称，optionsString 是该name的选项（路径，域）
delete_all_cookies(): 删除所有信息
'''

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.youdao.com')

# 获取cookie
cookie = driver.get_cookies()
print(cookie)

'''向浏览器中写入cookies信息'''
driver.add_cookie({'name':'key-aaaaa','value':'value-bbbbbb'})
# 遍历cookies 中的name和value信息并打印
for cookie in driver.get_cookies():
    print("%s-> %s"%(cookie['name'],cookie['value']))