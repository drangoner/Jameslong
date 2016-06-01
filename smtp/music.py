import urllib.request
import time

class music:

    def __init__(self,url):
        self.url = url


    def download(self):
        name = time.localtime()
        full_name = '/var/www/friends/music/'+str(name[0])+'-'+str(name[1])+'-'+str(name[2])+'2.mp3'
        urllib.request.urlretrieve(self.url,full_name)
mu = music('http://218.197.116.216/m10.music.126.net/20160601233028/668251d8f847e20bc78eee033f87d3b7/ymusic/8f48/c552/df0f/30b8555244d5dbada66cddbefcdd7e1a.mp3?wshc_tag=0&wsts_tag=574ef9b8&wsid_tag=decc0106&wsiphost=ipdbm')
mu.download()
