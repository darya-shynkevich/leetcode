# Given a zero-based permutation nums (0-indexed), build an array of the same length
# where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
#
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

# 1 <= nums.length <= 1000
# 0 <= nums[i] < nums.length
# The elements in nums are distinct.

from typing import List


class Solution:

    def buildArray(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)

        q = nums_len

        i = 0  # Turn each element from the array into a = qb + r
        while i < nums_len:
            new_index = nums[i]

            r = new_index

            b = nums[new_index] % q

            nums[i] = q * b + r

            i += 1

        i = 0
        while i < nums_len:
            nums[i] = nums[i] // q

            i += 1

        return nums


if __name__ == "__main__":
    solution = Solution()

    nums = [0, 2, 1, 5, 3, 4]

    assert solution.buildArray(nums=nums) == [0, 1, 2, 4, 5, 3]

    nums = [5, 0, 1, 2, 3, 4]

    assert solution.buildArray(nums=nums) == [4, 5, 0, 1, 2, 3]
