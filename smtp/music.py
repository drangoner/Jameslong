import urllib.request
import time

class music:

    def __init__(self,url):
        self.url = url


    def download(self):
        name = time.localtime()
        full_name = './music/'+str(name[0])+'-'+str(name[1])+'-'+str(name[2])+'.mp3'
        urllib.request.urlretrieve(self.url,full_name)
mu = music('http://218.197.116.216/m10.music.126.net/20160529131813/7de3df89d9f6287bc04945fe43ebbde2/ymusic/9fa6/6e8e/2605/2db7117e771988dd3fc816e634387c51.mp3?wshc_tag=0&wsts_tag=574a75b9&wsid_tag=decc0106&wsiphost=ipdbm')
mu.download()
