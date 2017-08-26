#一种更加有效的方法是，让 Selenium 不断地检查某个元素是否存
#在，以此确定页面是否已经完全加载，如果页面加载成功就执行后面的程序
from selenium import webdriver
# 下面的导入用 id 是 loadedButton 的按钮检查页面是不是已经完全加载
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  #expected_conditions 缩写


driver = webdriver.PhantomJS(executable_path='')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
driver.close()
