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
    # def countBits(self, n: int) -> List[int]:
    #
    #     # Time: O(n⋅log(n) / 2), Space: O(1)
    #
    #     result = [0]
    #
    #     for i in range(1, n + 1):
    #
    #         k = i
    #         hamming_distance = 0
    #         while k:
    #             k = k & (k - 1)
    #             hamming_distance += 1
    #
    #         result.append(hamming_distance)
    #
    #     return result

    # def countBits(self, n: int) -> List[int]:
    #
    #     # Time: O(n), Space: O(1)
    #
    #     ans = [0] * (n + 1)
    #     x = 0
    #     b = 1
    #
    #     # [0, b) is calculated
    #     while b <= n:
    #         # generate [b, 2b) or [b, n) from [0, b)
    #         while x < b and x + b <= n:
    #             ans[x + b] = ans[x] + 1
    #             x += 1
    #         x = 0  # reset x
    #         b = 2 * b
    #
    #     return ans

    # def countBits(self, n: int) -> List[int]:
    #
    #     # Time: O(n), Space: O(1)
    #
    #     ans = [0] * (n + 1)
    #     for x in range(1, n + 1):
    #         # x >> 1: x // 2
    #         # x & 1: x % 2
    #         ans[x] = ans[x >> 1] + (x & 1)
    #     return ans

    def countBits(self, n: int) -> List[int]:

        # Time: O(n), Space: O(1)

        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.countBits(n=2) == [0, 1, 1]

    assert solution.countBits(n=5) == [0, 1, 1, 2, 1, 2]
