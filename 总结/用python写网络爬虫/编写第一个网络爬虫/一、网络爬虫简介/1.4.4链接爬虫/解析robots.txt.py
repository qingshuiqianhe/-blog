'''解析robots.txt
>>>import robotparser
>>>rp = robotparser.RobotFileParser()
>>>rp.set_url('http://example.webscraping.com/robots.txt')
>>>rp.read()'''
# 将该功能集成到爬虫中，在crawl循环添加该检查
import urlparse
def link_crawler(seed_url,link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
while crawl_queue:
    url = crawl_queue.pop()
    # check url passes robots.txt restrctions
    if rp.can_fench(user_agent,url):
        html = download(url)
        for link in get_links(html):
            # check id link mathches expected regex
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                # check if have already seen this link
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)
    else:
        print 'Blocked by robots.txt',url