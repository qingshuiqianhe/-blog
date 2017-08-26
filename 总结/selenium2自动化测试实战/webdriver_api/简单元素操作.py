from selenium import webdriver
driver = webdriver.Chrome()
# driver.get('www.123.com')
# driver.find_element_by_id("input").clear()
# driver.find_element_by_id("input").send_keys("username")
# driver.find_element_by_id("pwdinput").clear()
# driver.find_element_by_id("pwdinput").send_keys("passwd")
# driver.find_element_by_id('loginBtn').click()
# '''126邮箱登陆'''

# submit 用于提交表单
driver.get('http://www.youdao.com')
driver.find_element_by_id('translateContent').send_keys('lol')
driver.find_element_by_id('translateContent').submit()