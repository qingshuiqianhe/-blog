# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
# 下面的导入用 id 是 loadedButton 的按钮检查页面是不是已经完全加载
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  #expected_conditions 缩写

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("selenium2")
# driver.find_element_by_id("su").click()
# driver.find_element_by_link_text("新闻")
# driver.quit()

'''查找定位大概语句  1;id 2:name 3:class 4:tag 5:link 6 ；partial link 7:XPATH '''
# 1 ID
# driver.find_element_by_id("ke")
# 2 name
# driver.find_element_by_name("wd")
# 3 class  s  二者结果如下，element 是把标签拿出来了，elements把标签放在了列表里？？
# c = driver.find_element_by_class_name("c-tips-container")
# d = driver.find_elements_by_class_name("c-tips-container")
# c = <selenium.webdriver.remote.webelement.WebElement (session="16b695e5e976041f5ac20d94cc455ebc", element="0.6945089916666247-1")>
# d = [<selenium.webdriver.remote.webelement.WebElement (session="16b695e5e976041f5ac20d94cc455ebc", element="0.6945089916666247-1")>]

# 4 tag
# driver.find_element_by_tag_name("wd")
# driver.find_elements_by_tag_name("wd")
# 5 link
# driver.find_element_by_link_text("")
# driver.find_elements_by_link_text("")

# 6有些文本链接比较长，通过一部分定位
#  eg: <a class="mnav" name="tj_lang" href="#"  一个很长的文本链接 </a>>
# driver.find_element_by_partial_link_text("一个很长的")
# driver.find_element_by_partial_link_text("文本链接")

# 7 XPath   在xml中定位 练习使用firebug 右键中的xpath
    # 7.1 绝对路径定位eg： 百度中找到输入框和搜索按钮
# driver.find_element_by_xpath("/html/body/div/div[2]/div/div/from/span/input")
# driver.find_element_by_xpath("/html/body/div/div[2]/div/div/from/span[2]/input")

    #7.2 利用元素属性定位
# driver.find_element_by_xpath("//input[@id='kw']")
# driver.find_element_by_xpath("//input[@id='su']")
    # 不指定标签名的情况
#driver.find_element_by_xpath("//*[@id='su']")

# 8 css定位
    #8.1 css 属性定位,没有这个属性了
    #d = driver.find_element_by_class_selector(".bgs_btm")
    #结果：'WebDriver' object has no attribute 'find_element_by_class_selector'
try:
    f = driver.find_element_by_class_name("s_ipt")
    print('f',f)
except Exception as e:
    print(e)

# 貌似css 只有这一个
#driver.find_element_by_class_name("#kw")

# 9  By.ID
#driver.find_element(By.ID,"kw")
#<selenium.webdriver.remote.webelement.WebElement
# (session="ef5c3ef84a3f4f50a332255ab6594195", element="0.6701959143153386-1")>

#一种更加有效的方法是，让 Selenium 不断地检查某个元素是否存
#在，以此确定页面是否已经完全加载，如果页面加载成功就执行后面的程序
# driver = webdriver.PhantomJS(executable_path='')
# driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# try:
#     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
# finally:
#     print(driver.find_element_by_id("content").text)
# driver.close()


