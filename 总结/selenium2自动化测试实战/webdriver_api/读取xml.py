from  xml.dom import minidom
# 打开xml文档
dom = minidom.parse('info.xml')
# 得到文档对象
root = root.documentElement
tagname = root.getElementsByTagName('browser')
print(tagname[0].tagName)
tagname = root.getElementsByTagName('login')
print(tagname[1].tagName)
tagname = root.getElementsByTagName('province')# 获得标签名为“province” 的一组标签
print(tagname[2].tagName)


'''结果
browser
login
province'''

# 获得标签的属性值
from  xml.dom import minidom
# 打开xml文档
dom = minidom.parse('info.xml')
# 得到文档对象
root = root.documentElement
logins = root.getElementsByTagName('login')

username = logins[0].getAttribute("username")
print(username)
password = logins[0].getAttribute('password')
print(password)


username = logins[1].getAttribute("username")
print(username)
password = logins[1].getAttribute('password')
print(password)
'''
admin
123456
quest
654321'''



'''标签对之间的信息'''
from  xml.dom import minidom
# 打开xml文档
dom = minidom.parse('info.xml')
# 得到文档对象
root = root.documentElement

provinces = dom.getElementsByTagName('province')
citys = dom.getElementsByTagName('city')

p2 = provinces[1].firstChild.data
print(p2)

c1 = citys[0].firstChild.data
print(c1)

c2 = citys[0].firstChild.data
print(c2)
'''
广东
深圳
珠海'''


