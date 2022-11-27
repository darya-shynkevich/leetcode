# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
#
# Return the answer in an array.
import math
# Constraints:
#
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_hashmap = {}

        for i, num in enumerate(sorted(nums)):
            nums_hashmap[num] = min(nums_hashmap.get(num, math.inf), i)

        result = []
        for num in nums:
            result.append(nums_hashmap[num])

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]

    assert solution.smallerNumbersThanCurrent(nums=[6, 5, 4, 8]) == [2, 1, 0, 3]

    assert solution.smallerNumbersThanCurrent(nums=[7, 7, 7, 7]) == [0, 0, 0, 0]
