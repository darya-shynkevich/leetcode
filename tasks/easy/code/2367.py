# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
# A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
#
# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

# Constraints:
#
# 3 <= nums.length <= 200
# 0 <= nums[i] <= 200
# 1 <= diff <= 50
# nums is strictly increasing.
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    assert solution.arithmeticTriplets(nums=[0, 1, 4, 6, 7, 10], diff=3) == 2

    assert solution.arithmeticTriplets(nums=[4, 5, 6, 7, 8, 9], diff=2) == 2
