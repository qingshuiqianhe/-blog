# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
# 2
from time import sleep ,ctime
# 3隐式等待
from selenium.common.exceptions import NoSuchElementException
# 显示等待
driver = webdriver.Chrome()
#driver.get("http://www.baidu.com")
# # (driver ,timeout=最长等待时间，poll_frequency=检测的步长）。配合until(method,message='' 使用或者until_not
# # )调用该方法提供的驱动程序作为一个参数，直到返回值为TRUE
# element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'kw')))
# element.send_keys('selenium')

#driver.quit()

# 2is_display
# print(ctime())
# for i in range(10):
#     try:
#         el = driver.find_element_by_id('kw22')
#         if el.is_display():
#             break
#     except:pass
#     sleep(1)
# else:
#     print("time out")
# driver.close()
# print(ctime())


'''隐式等待'''
driver.implicitly_wait(10)# 等待10s
driver.get("http://www.baidu.com")
try:
    print(ctime())
    driver.find_element_by_id('kw22').send_keys('selenium')
except NoSuchElementException as e :
    print(e)
finally:
    print(ctime())
    driver.quit()



'''sleep'''