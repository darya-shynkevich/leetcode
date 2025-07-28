import random


class RandomizedSet:

    def __init__(self):
        self.storage = []
        self.storage_search = {}
        self.storage_len = 0

    def insert(self, val: int) -> bool:
        if val in self.storage_search:
            return False
        self.storage.append(val)
        self.storage_len += 1

        self.storage_search[val] = self.storage_len - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.storage_search:
            return False

        index = self.storage_search[val]
        self.storage.pop(index)
        self.storage_len -= 1
        del self.storage_search[val]
        return True

    def getRandom(self) -> int:
        random_index = random.randint(0, self.storage_len - 1)
        return self.storage[random_index]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
obj.insert(1)
obj.insert(1)
obj.insert(1)
obj.remove(1)
print(obj.getRandom())