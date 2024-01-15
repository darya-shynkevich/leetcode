from collections import OrderedDict
from loguru import logger


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key=key)

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def get(self, key):
        value = self.cache.get(key)
        if value is not None:
            self.cache.move_to_end(key=key)
            return value

        return -1


if __name__ == "__main__":
    lru_cache = LRUCache(capacity=2)

    lru_cache.put(1, 1)
    lru_cache.put(2, 2)

    logger.info(lru_cache.get(2))
    logger.info(lru_cache.get(1))
    logger.info(lru_cache.get(3))

    lru_cache.put(3, 3)
    logger.info(lru_cache.get(2))
    logger.info(lru_cache.get(1))
    logger.info(lru_cache.get(3))
