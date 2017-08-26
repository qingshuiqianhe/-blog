# coding:utf-8
from selenium import webdriver
# 引入ActionChains
from selenium.webdriver.common.action_chains import  ActionChains
driver = webdriver.Chrome()
driver.get("www.sina.com")

# 定位到要右击的元素
right_click = driver.find_element_by_id('xx')
# 对定位到的元素进行操作
ActionChains(driver).context_click(right_click).perform()



'''悬停'''
above = driver.find_element_by_id("id")
ActionChains(driver).move_to_element(above).perform()

'''双击'''
double_click = driver.find_element_by_id("id")
ActionChains(driver).double_click(double_click).perform()

'''拖放
drag_and_drop( source ,target)在源元素上按住鼠标左键，然后移动到目标元素上释放
source ： 鼠标拖动的源元素
target ： 鼠标释放操作'''
'''考虑考虑实现那种图片认证的程序，这个可能不太适合，by'id的方法，
获取拖动的开始元素位置，加载图片，识别图的颜色缺失部分产生相对的位置，移动相对位置'''
# 定位元素的原始位置
element = driver.find_element_by_id("xx")
# 定位要移动的相对位置
target = driver.find_element_by_id("new xx")
# 执行拖放操作
ActionChains(driver).drag_and_drop(element,target).perform()

