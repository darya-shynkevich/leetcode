from math import inf
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        result = inf

        left, right, current_sum = 0, 0, 0

        while right < n:
            current_sum += nums[right]
            right += 1

            while current_sum >= target:
                result = min(result, right - left)
                current_sum -= nums[left]
                left += 1

        return 0 if result == inf else result


solution = Solution()
print(solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
