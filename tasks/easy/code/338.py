# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
# ans[i] is the number of 1's in the binary representation of i.

# Constraints:
#
# 0 <= n <= 105

# Follow up:
# 1. It is very easy to come up with a solution with a runtime of O(n log n).
# Can you do it in linear time O(n) and possibly in a single pass?
# 2. Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        pass


if __name__ == '__main__':
    solution = Solution()

    assert solution.countBits(n=2) == [0, 1, 1]

    assert solution.countBits(n=5) == [0, 1, 1, 2, 1, 2]
