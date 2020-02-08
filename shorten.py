import redis
import random

class URL_Shortener:

    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost',
                                       port=6379,
                                       db=0)

    def __get_short_id(self, url):
        id = "".join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 5))
        return id

    def short(self, long_url):
        id = self.__get_short_id(long_url)
        short_url = "http://127.0.0.1:5000/urls/{}".format(id)

        try:
            self.redis.set(id, long_url)
            return True, id
        except:
            return False

    def get_long_url(self, id):
        try:
            return True, self.redis.get(id)
        except:
            return False