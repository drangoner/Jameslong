import urllib.request
import time

class music:

    def __init__(self,url):
        self.url = url


    def download(self):
        name = time.localtime()
        full_name = '/var/www/friends/music/'+str(name[0])+'-'+str(name[1])+'-'+str(name[2])+'.mp3'
        urllib.request.urlretrieve(self.url,full_name)
mu = music('http://218.197.116.216/m10.music.126.net/20160601224536/43bd341360d4ade3dea346af56748c6a/ymusic/f0a4/6fdb/60ef/0c6d0b846c57e3bf52ec1a4d9141c540.mp3?wshc_tag=0&wsts_tag=574eef35&wsid_tag=decc0106&wsiphost=ipdbmX')
mu.download()
