from math import inf
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        left, right = 0, k - 1

        min_diff = inf

        while right < len(nums):
            min_diff = min(min_diff, nums[right] - nums[left])
            right += 1
            left += 1

        return min_diff


solution = Solution()
print(solution.minimumDifference(nums=[90], k=1))
print(solution.minimumDifference(nums=[9, 4, 1, 7], k=2))
