import urllib.request
import time

class music:

    def __init__(self,url):
        self.url = url


    def download(self):
        name = time.localtime()
        full_name = '/var/www/friends/music/'+str(name[0])+'-'+str(name[1])+'-'+str(name[2])+'.mp3'
        urllib.request.urlretrieve(self.url,full_name)
mu = music('http://218.197.116.216/m10.music.126.net/20160603231222/783798e0e18b12d70bb396e88b72676f/ymusic/ea85/1604/cd01/2b1dbb7127cb8a84eb0ef39dce33efea.mp3?wshc_tag=1&wsts_tag=5751987b&wsid_tag=decc0106&wsiphost=ipdbm')
mu.download()
