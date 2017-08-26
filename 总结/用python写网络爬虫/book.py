# coding=utf-8
'''估计网站大小
1.google  搜索： site:examplewebscraping.com
2 在域名后面加上URL路径，可以对结果进行过滤，仅显示网站的某些部分。site:examplewebscraping.com/view   仅显示国家页面
'''
'''识别网站所用技术   pio install builtwith
import builtwith
bulitwith.parse("url")


寻找网站的所有者
pip install pyhton_whois
>>>import whois
>>>print whois.whois("appspot.com")



'''
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

#发生错误记录次数，当错误在500---6000之间时计数，并且尝试三次
def download(url,num_retries=2):
    print ('download ', url)
    try:
        html = urlllib2.urlopen(url).read()
    except urlllib2.URLError as e:
        print ('download error',e.reason)
        html = None
        if num_retries >0:
            if hasattr(e,'code') and 500<= e.code <600:
                return download(url,num_retries-1)
    return html


# 设置代理
def download(url,user_agent='wswp',num_retries=2):
    print ("download:",url)
    headers = {'User_agent':user_agent}
    request = urlllib2.Request(url,headers=headers)
    try:
        html = urlllib2.urlopen(request).read()
    except urlllib2.URLError as e :
        print ("doenload error",e.reason)
        html = None
        if num_retries >0:
            if hasattr(e,'code') and 500<= e.code <600:
                return download(url,user_agent,num_retries-1)
    return html


'''css 选择器'''
def crawl_sitemap(url):
    # 下载网站地图文件
    sitemap = doenlaod(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>',sitemap)
    # 下载每个链接
    for link in links :
        html = download(link)
'''id 遍历爬虫'''
import  itertools
for page in itertools.count(1):
    url = 'http://example/webscrapin.com/view/-%d' %page
    html = download(url)
    if html in None:
        break
    else:
        # success -can scrape the result
        pass


'''链接爬虫'''
import re
def link_crawler(seed_url,kink_reqex):
    '''crawl from thw given seed url following links matched by link_regex'''
    crawl_queue = [seed_url]
    while crawl_queue:
        url =crawl_queue.pop()
        html = download(url)
        # filter for links matching our regular regular ecperession
        for link in get_links(html):
            if re.match(link_regex,link):
                crawl_queue.append(link)
def get_links(html):
    '''return a list of links from html'''
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return  webpage_regex.findall(html)


'''获取所有地点，并如期停止，实用'''
import urlparse
def link_crawler(seed_url,link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            # check id link mathches expected regex
            if re.match(link_regex ,link):
                link = urlparse.urljoin(seed_url,link)
                # check if have already seen this link
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)


'''解析robots.txt
>>>import robotparser
>>>rp = robotparser.RobotFileParser()
>>>rp.set_url('http://example.webscraping.com/robots.txt')
>>>rp.read()



22'''
# 正则表达式
import re
url = 'http://example.webscraping.com.view/United-Kingdom-239'
html = download(url)