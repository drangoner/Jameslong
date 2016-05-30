import urllib.request
import time

class music:

    def __init__(self,url):
        self.url = url


    def download(self):
        name = time.localtime()
        full_name = '/var/www/friends/music/'+str(name[0])+'-'+str(name[1])+'-'+str(name[2])+'.mp3'
        urllib.request.urlretrieve(self.url,full_name)
mu = music('http://218.197.116.216/m10.music.126.net/20160530170357/2d97d1ecd1fdeb3f37c3a6becb138609/ymusic/1c6e/2061/9d1b/5ad16b1b5fff0f55c95a6fc0ef873207.mp3?wshc_tag=0&wsts_tag=574bfc22&wsid_tag=decc0106&wsiphost=ipdbm')
mu.download()
