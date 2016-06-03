import urllib.request
import time

class music:

    def __init__(self,url):
        self.url = url


    def download(self):
        name = time.localtime()
        full_name = '/var/www/friends/music/'+str(name[0])+'-'+str(name[1])+'-'+str(name[2])+'.mp3'
        urllib.request.urlretrieve(self.url,full_name)
mu = music('http://222.204.1.115/20160603230726/0d96272d6c7669fd6de3c8dcbc82cabc/ymusic/bdb6/4eb6/aabd/26e833f3fe2e76237b2ef5f815077ffb.mp3?&ncs_hash_key_one=e6&ncs_hash_key_two=3b&ncs_hash_key=e63ba781365bde6ebd8a73c0d4560072&ncs_dir=0003/163cloudnmusic&')
mu.download()
