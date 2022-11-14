# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i]
# and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#
# Specifically, ans is the concatenation of two nums arrays.
#
# Return the array ans.

# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 1]

    assert solution.getConcatenation(nums=nums) == [1, 2, 1, 1, 2, 1]

    nums = [1, 3, 2, 1]

    assert solution.getConcatenation(nums=nums) == [1, 3, 2, 1, 1, 3, 2, 1]
