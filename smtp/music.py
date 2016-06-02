import urllib.request
import time

class music:

    def __init__(self,url):
        self.url = url


    def download(self):
        name = time.localtime()
        full_name = '/var/www/friends/music/'+str(name[0])+'-'+str(name[1])+'-'+str(name[2])+'.mp3'
        urllib.request.urlretrieve(self.url,full_name)
mu = music('218.197.116.217/m10.music.126.net/20160602231527/7e9d30ead0001c867d4ca6f350f91494/ymusic/7c61/821d/3107/62a76dbbfefaf0be8347bf24603c63df.mp3?wshc_tag=0&wsts_tag=575047b4&wsid_tag=decc0106&wsiphost=ipdbm')
mu.download()
