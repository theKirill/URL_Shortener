import redis
import random

class URL_Shortener:

    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost',
                                       port=6379,
                                       db=0)

    def __get_short_id(self):
        id = "".join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 5))
        return id

    def __save_to_db(self, id, long_url):
        try:
            self.redis.set(id, long_url)
            return True, id
        except:
            return False, 'null'

    def short(self, long_url):
        id = self.__get_short_id()

        return self.__save_to_db(id, long_url)

    def get_long_url(self, id):
        try:
            return True, self.redis.get(id)
        except:
            return False, 'null'