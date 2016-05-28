import urllib.request
from bs4 import BeautifulSoup
import time
from urllib.error import URLError


class zhihu:

    def __init__(self):
        self.url = 'http://daily.zhihu.com'
        self.user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'
        self.headers = {'User-Agent': self.user_agent}

    def getPage(self,url):
        """
        Get the page of the url.
        :return: html
        """
        try:
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            page = response.read().decode('utf-8')
            return page
        except URLError as e:
            if hasattr(e, "reason"):
                print("connect failed ",e.reason)
                return None

    def getContent(self):
        html = self.getPage(self.url)
        if(html):
            soup = BeautifulSoup(html, 'html5lib')
            content_url = self.url + soup.select(".wrap")[0].a['href']
            content_html =self.getPage(content_url)
            soup = BeautifulSoup(content_html, 'html5lib')
            pic = soup.select('.img-wrap')[0]#获取图片
            text = soup.select('.content')[0]#获取文字
            result =str(pic) + str(text)
            return result