# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# Implement the MovingAverage class:
#
# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.

# 1 <= size <= 1000
# -105 <= val <= 105
# At most 104 calls will be made to next.


class MovingAverage:

    def __init__(self, size: int):
        self.window_size = size

        self.prev_sum = 0
        self.count = 0

        self.history = []

    def next(self, val: int) -> float:

        self.history.append(val)

        if self.count < self.window_size:
            self.count = self.count + 1
            self.prev_sum = self.prev_sum + val
        else:
            len_history = len(self.history)
            self.history = self.history[len_history - self.window_size: len_history]
            self.prev_sum = sum(self.history)

        return round(self.prev_sum / self.count, 5)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


if __name__ == "__main__":
    solution = MovingAverage(size=3)

    assert solution.next(1) == 1  # return 1.0 = 1 / 1
    assert solution.next(10) == 5.5  # return 5.5 = (1 + 10) / 2
    assert solution.next(3) == 4.66667  # return 4.66667 = (1 + 10 + 3) / 3
    assert solution.next(5) == 6.0  # return 6.0 = (10 + 3 + 5) / 3
