#coding= utf-8
import urllib2
import re
import datetime

'''代理'''
def download(url,user_agent='wswp',proxy=None,num_retries=2):
    print ("downloading",url)
    headers = {"User_agent":user_agent}
    requwst = urllib2.Request(url,headers=headers)


    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHander(proxy_params))
    try:
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print ("download error",e.reason)
        html = None
        if num_retries >0:
            if hasattr(e,'code') and 500 <=e.code <600:
                html = download(url,user_agent,proxy,num_retries-1)
    return html

'''下载限速'''

class Throttle:
    '''add a delay between downloads to the same domain'''
    def __init__(self):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self,url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay >0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now()-last_accessed).seconds
            if sleep_secs >0:
                # domain has been accessed recently so need to sleep
                time.sleep(sleep_secs)
        # update the last accessed time
        self.domains[domain] = datetime.datetime.now()


'''在每次下载之前调用该函数，有效防止下载过快'''
throttle = Throttle(delay)
''''''
throttle.wait(url)
result = download(url,headers,proxy=proxy,num_retries=num_retries)

'''避免陷阱，设置深度'''
def link_crawler(url,max_depth = 2):
    max_depth = 2
    seen = {}
    '''...'''
    depth =  seen[url]
    if depth != max_depthz:
        if link not in links :
            seen[link] = depth+1
            crawler_queue.append(link)
















