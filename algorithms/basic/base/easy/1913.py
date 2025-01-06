# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
#
# For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
# Given an integer array nums, choose four distinct indices w, x, y, and z such that the product
# difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
#
# Return the maximum such product difference.

# Constraints:
#
# 4 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^4
from typing import List


class Solution:
    # def maxProductDifference(self, nums: List[int]) -> int:
    #     Time: O(n log(n)), Space: O(1)
    #     nums.sort()
    #     return nums[-1] * nums[-2] - nums[0] * nums[1]

    def maxProductDifference(self, nums: List[int]) -> int:

        # Time: O(n), Space: O(1)

        min1 = min2 = float('inf')
        max1 = max2 = float('-inf')

        for number in nums:
            if number <= min1:
                min1, min2 = number, min1
            elif number < min2:
                min2 = number

            if number >= max1:
                max1, max2 = number, max1
            elif number > max2:
                max2 = number

        return max1 * max2 - min1 * min2


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxProductDifference(nums=[5, 6, 2, 7, 4]) == 34

    assert solution.maxProductDifference(nums=[4, 2, 5, 9, 7, 4, 8]) == 64

