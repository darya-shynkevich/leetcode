# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Constraints:
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9

# Follow-up: Could you solve the problem in linear time and in O(1) space?
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Time: O(Nlog(N)), Space: O(1)

        if len(nums) == 1:
            return nums[0]

        max_element = prev_element = None
        max_element_count = current_element_count = 0

        nums.sort()

        for num in nums:
            if num == prev_element:
                current_element_count += 1
            else:
                current_element_count = 0

            if current_element_count > max_element_count:
                max_element_count = current_element_count
                max_element = num

            prev_element = num

        return max_element


if __name__ == "__main__":
    solution = Solution()

    assert solution.majorityElement(nums=[3, 2, 3]) == 3

    assert solution.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]) == 2

    assert solution.majorityElement(nums=[1]) == 1
