from loguru import logger


class Item:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Key: {self.key}, value: {self.value}"


class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def show(self):
        return [item for item in self.table if item]

    def hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        key_hash = self.hash(key=key)
        for item in self.table[key_hash]:
            if item.key == key:
                item.value = value
                return

        self.table[key_hash].append(Item(key, value))

    def get(self, key):
        key_hash = self.hash(key=key)
        for item in self.table[key_hash]:
            if item.key == key:
                return item.value

        raise ValueError(f'Key {key} is not found in {self.table}')

    def delete(self, key):
        key_hash = self.hash(key=key)
        for index, item in enumerate(self.table[key_hash]):
            if item.key == key:
                del self.table[key_hash][index]
                return item.value

        raise ValueError(f'Key {key} is not found in {self.table}')


if __name__ == "__main__":
    hash_table = HashTable(size=100)
    hash_table.set(1, 1)
    hash_table.set(2, 2)
    hash_table.set(3, 3)
    hash_table.set(4, 4)

    logger.info(hash_table.get(2))

    logger.info(hash_table.delete(3))

    logger.info(hash_table.show())