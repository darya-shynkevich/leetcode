# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
#
# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums.
#
# Note: Subsets with the same elements should be counted multiple times.
#
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

# Constraints:
#
# 1 <= nums.length <= 12
# 1 <= nums[i] <= 20


from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    assert solution.subsetXORSum(nums=[1, 3]) == 6

    assert solution.subsetXORSum(nums=[5, 1, 6]) == 28

    assert solution.subsetXORSum(nums=[3, 4, 5, 6, 7, 8]) == 480
