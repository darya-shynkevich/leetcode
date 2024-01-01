# Given an integer n, return true if and only if it is an Armstrong number.
#
# The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.
import math


# Constraints:
#
# 1 <= n <= 10^8

class Solution:
    def isArmstrong(self, n: int) -> bool:
        input_number = n

        # Time: O(N), Space: O(1)

        n_len = int(math.log10(n) + 1)
        result = 0
        while n:
            current_number = n % 10
            result += current_number ** n_len
            n = n // 10

        return result == input_number


if __name__ == "__main__":
    solution = Solution()

    assert solution.isArmstrong(n=153) is True

    assert solution.isArmstrong(n=123) is False
