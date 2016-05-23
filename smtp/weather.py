import urllib.request
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import io
import sys

class weather:

    def __init__(self,url):
        self.url = url
        self.user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'
        self.headers = {'User-Agent' : self.user_agent}

    def getPage(self):
        try:
            request = urllib.request.Request(self.url, headers=self.headers)
            response = urllib.request.urlopen(request)
            return response.read().decode('utf-8')
        except URLError as e:
            if hasattr(e, "reason"):
                print('链接失败',e.reason)
                return None

    def getContent(self):
        page = self.getPage()
        soup = BeautifulSoup(page, "html5lib")
        return(soup.select('ul.t'))

