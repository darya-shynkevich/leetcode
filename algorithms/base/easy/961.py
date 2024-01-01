# You are given an integer array nums with the following properties:
#
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

# Constraints:
#
# 2 <= n <= 5000
# nums.length == 2 * n
# 0 <= nums[i] <= 104
# nums contains n + 1 unique elements and one of them is repeated exactly n times.
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        # Time: O(N), Space: O(N)

        nums_set = set()
        for num in nums:
            if num in nums_set:
                return num

            nums_set.add(num)


if __name__ == "__main__":
    solution = Solution()

    assert solution.repeatedNTimes(nums=[1, 2, 3, 3]) == 3

    assert solution.repeatedNTimes(nums=[2, 1, 2, 5, 3, 2]) == 2

    assert solution.repeatedNTimes(nums=[5, 1, 5, 2, 5, 3, 5, 4]) == 5
