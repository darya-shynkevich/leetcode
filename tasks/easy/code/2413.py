# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

# 1 <= n <= 150


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2


if __name__ == "__main__":
    solution = Solution()

    assert solution.smallestEvenMultiple(n=5) == 10

    assert solution.smallestEvenMultiple(n=6) == 6
