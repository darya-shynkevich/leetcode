# Given the array of integers nums, you will choose two different indices i and j of that array.
# Return the maximum value of (nums[i]-1)*(nums[j]-1).

# Constraints:
#
# 2 <= nums.length <= 500
# 1 <= nums[i] <= 10^3
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Time: O(N * log(N)), Space: O(1)

        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxProduct(nums=[3, 4, 5, 2]) == 12

    assert solution.maxProduct(nums=[1, 5, 4, 5]) == 16

    assert solution.maxProduct(nums=[3, 7]) == 12
