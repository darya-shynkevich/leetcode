# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0
        for num in nums:
            temp ^= num

        return temp


if __name__ == "__main__":
    solution = Solution()

    assert solution.singleNumber(nums=[2, 2, 1]) == 1

    assert solution.singleNumber(nums=[4, 1, 2, 1, 2]) == 4

    assert solution.singleNumber(nums=[1]) == 1
