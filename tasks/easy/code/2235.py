# Given two integers num1 and num2, return the sum of the two integers.
#
# -100 <= num1, num2 <= 100


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


if __name__ == "__main__":
    solution = Solution()

    assert solution.sum(num1=12, num2=5) == 17

    assert solution.sum(num1=-10, num2=4) == -6
