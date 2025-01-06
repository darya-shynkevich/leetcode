# There is a stream of n (idKey, value) pairs arriving in an arbitrary order,
# where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.
#
# Design a stream that returns the values in increasing order of their IDs by returning a chunk (list)
# of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.
#
# Implement the OrderedStream class:
#
# OrderedStream(int n) Constructs the stream to take n values.
# String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream,
# then returns the largest possible chunk of currently inserted values that appear next in the order.

# Constraints:
#
# 1 <= n <= 1000
# 1 <= id <= n
# value.length == 5
# value consists only of lowercase letters.
# Each call to insert will have a unique id.
# Exactly n calls will be made to insert.

from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.data = [None] * n
        self.ptr = 0  # 0-indexed

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.data[idKey] = value
        if idKey > self.ptr:
            return []

        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr += 1

        return self.data[idKey:self.ptr]


if __name__ == "__main__":
    # Your OrderedStream object will be instantiated and called as such:
    os = OrderedStream(5)

    os.insert(3, "ccccc")
    os.insert(1, "aaaaa")
    os.insert(2, "bbbbb")
    os.insert(5, "eeeee")
    os.insert(4, "ddddd")
