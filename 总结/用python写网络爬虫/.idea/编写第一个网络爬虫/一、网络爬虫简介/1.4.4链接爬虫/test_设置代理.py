#coding=utf-8
import urllib2
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