# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
#
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.
#
# It is guaranteed that the insertion operations will be valid.
#
# Constraints:
#
# 1 <= nums.length, index.length <= 100
# nums.length == index.length
# 0 <= nums[i] <= 100
# 0 <= index[i] <= i

from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        if not nums or not index: return []

        result = []
        for n, i in zip(nums, index):
            print(result, i, n)
            result.insert(i, n)

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]) == [0, 4, 1, 3, 2]

    assert solution.createTargetArray(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]) == [0, 1, 2, 3, 4]

    assert solution.createTargetArray(nums=[1], index=[0]) == [1]

    assert solution.createTargetArray(nums=[4, 2, 1, 1], index=[0, 0, 2, 0]) == [1, 2, 4, 1]

    assert solution.createTargetArray(nums=[4, 2, 4, 3, 2], index=[0, 0, 1, 3, 1]) == [2, 2, 4, 4, 3]
