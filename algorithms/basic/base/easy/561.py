# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
#
# Constraints:
#
# 1 <= n <= 104
# nums.length == 2 * n
# -104 <= nums[i] <= 104

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__ == "__main__":
    solution = Solution()

    assert solution.arrayPairSum(nums=[1, 4, 3, 2]) == 4

    assert solution.arrayPairSum(nums=[6, 2, 6, 5, 1, 2]) == 9
