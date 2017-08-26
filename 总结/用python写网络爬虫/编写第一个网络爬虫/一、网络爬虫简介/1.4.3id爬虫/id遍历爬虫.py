#coding= utf-8
import urllib2
import  itertools
for page in itertools.count(1):
    url = 'http://example/webscrapin.com/view/-%d' %page
    html = download(url)
    if html in None:
        break
    else:
        # success -can scrape the result
        pass


# 对id遍历，有可能有的id被删除，数据库id的不连续，改进
# 设置最大允许的下载错误次数
max_errors =5
# 初始化下载错误值
num_errors = 0
for page in itertools.count(1):
    url = 'http://example/webscrapin.com/view/-%d' % page
    html = download(url)
    if html in None:
        # 收到错误并尝试重新下载网页
        num_errors +=1
        if num_errors == max_errors:
            break
    else:
        num_errors = 0