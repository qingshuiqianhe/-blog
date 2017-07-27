# coding=utf-8
#  py 2.7
import urllib2
def download(url):
    print ('downloading' ,url)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print ('download error ',e.reason)
        html = None
    return html
# 能捕获异常并返回none