import redis
import random

class URL_Shortener:

    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost',
                                       port=6379,
                                       db=0)

    def __get_short_code(self, url):
        code = "".join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 5))
        return code

    def short(self, long_url):
        code = self.__get_short_code(long_url)
        short_url = "http://127.0.0.1:5000/urls/{}".format(code)

        try:
            self.redis.set(code, long_url)
            return True, code
        except:
            return False

    def get_long_url(self, code):
        try:
            return True, self.redis.get(code)
        except:
            return False