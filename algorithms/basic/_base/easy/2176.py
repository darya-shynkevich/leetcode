# Given a 0-indexed integer array nums of length n and an integer k,
# return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i], k <= 100
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        # Time: O(N^2), Space: O(1)

        n = len(nums)
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and i * j % k == 0:
                    result += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.countPairs(nums=[3, 1, 2, 2, 2, 1, 3], k=2) == 4

    assert solution.countPairs(nums=[1, 2, 3, 4], k=1) == 0
