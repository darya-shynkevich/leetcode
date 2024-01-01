# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# Implement the MovingAverage class:
#
# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.

# 1 <= size <= 1000
# -105 <= val <= 105
# At most 104 calls will be made to next.


import collections


class MovingAverage:
    def __init__(self, size: int):
        self.window_size = size

        self.count = 0

        self.history = collections.deque()

    def next(self, val: int) -> float:

        self.history.append(val)

        if self.count < self.window_size:
            self.count = self.count + 1
        else:
            self.history.popleft()

        return round(sum(self.history) / self.count, 5)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


if __name__ == "__main__":
    solution = MovingAverage(size=3)

    assert solution.next(1) == 1  # return 1.0 = 1 / 1
    assert solution.next(10) == 5.5  # return 5.5 = (1 + 10) / 2
    assert solution.next(3) == 4.66667  # return 4.66667 = (1 + 10 + 3) / 3
    assert solution.next(5) == 6.0  # return 6.0 = (10 + 3 + 5) / 3
