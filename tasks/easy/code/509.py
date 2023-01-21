# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
#
# Given n, calculate F(n).

# Constraints:
#
# 0 <= n <= 30

class Solution:

    def __init__(self):
        self.result = 0

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == "__main__":
    solution = Solution()

    assert solution.fib(n=2) == 1

    assert solution.fib(n=3) == 2

    assert solution.fib(n=4) == 3
