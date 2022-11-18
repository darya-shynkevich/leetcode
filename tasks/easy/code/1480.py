# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        nums_len = len(nums)

        for i in range(1, nums_len):
            nums[i] = nums[i] + nums[i - 1]

        return nums


if __name__ == "__main__":
    solution = Solution()

    assert solution.runningSum(nums=[1, 2, 3, 4]) == [1, 3, 6, 10]

    assert solution.runningSum(nums=[1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
