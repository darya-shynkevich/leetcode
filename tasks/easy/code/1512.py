# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

from math import factorial
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # C(n, 2) = n!/(2! * (n - 2)!).

        counter = {}
        for num in nums:
            num_count = counter.get(num) or 0
            counter.update({num: num_count + 1})

        result = 0
        for value in counter.values():
            if value <= 1:
                continue
            elif value == 2:
                result += 1
            else:
                result += factorial(value) / (2 * factorial(value - 2))

        return int(result)


if __name__ == "__main__":
    solution = Solution()

    assert solution.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]) == 4

    assert solution.numIdenticalPairs(nums=[1, 1, 1, 1]) == 6

    assert solution.numIdenticalPairs(nums=[1, 2, 3]) == 0

    assert solution.numIdenticalPairs(nums=[1, 5, 3, 2, 4, 2, 5, 2, 2, 6, 6, 2, 4, 4, 5, 1, 5]) == 21
