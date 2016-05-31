import urllib.request
import time

class music:

    def __init__(self,url):
        self.url = url


    def download(self):
        name = time.localtime()
        full_name = '/var/www/friends/music/'+str(name[0])+'-'+str(name[1])+'-'+str(name[2])+'.mp3'
        urllib.request.urlretrieve(self.url,full_name)
mu = music('http://218.197.116.216/m10.music.126.net/20160531134412/53f458cb416f7c7876a1a670ac7cd9b4/ymusic/66ac/d21f/2b8b/e420aa20de79bb87b6811eb0db99c322.mp3?wshc_tag=0&wsts_tag=574d1ed1&wsid_tag=decc0106&wsiphost=ipdbm')
mu.download()
