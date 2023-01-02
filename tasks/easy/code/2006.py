# Given an integer array nums and an integer k, return the number of pairs (i, j)
# where i < j such that |nums[i] - nums[j]| == k.
#
# The value of |x| is defined as:
#
# x if x >= 0.
# -x if x < 0.

# Constraints:
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 1 <= k <= 99
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = {}
        for num in nums:
            current_count = counter.get(num, 0)
            counter.update({num: current_count + 1})

        result = 0
        for num in nums:
            count = counter.get(num - k)
            if count:
                result += count

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.countKDifference(nums=[1, 2, 2, 1], k=1) == 4

    assert solution.countKDifference(nums=[1, 3], k=3) == 0

    assert solution.countKDifference(nums=[3, 2, 1, 5, 4], k=2) == 3
