#coding= utf-8
import urllib2
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

'''会得到错误，问题在下载index/1的时候，该链接只有网页的路径部分，没有协议和服务器部分，是一个相对链接。urllib2 无法获知上下文
将该链接转换为绝对链接，使用urlparse'''
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
'''可能陷入无限循环当中，修改采用set'''



