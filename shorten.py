import redis
import random
import os

class URL_Shortener:

    def __init__(self):
        redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
        self.redis = redis.from_url(redis_url)

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