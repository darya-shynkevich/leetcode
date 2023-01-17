# Given an integer array nums, move all the even integers at the beginning
# of the array followed by all the odd integers.
#
# Return any array that satisfies this condition.

# Constraints:
#
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000
from typing import List


class Solution:

    # def sortArrayByParity(self, nums: List[int]) -> List[int]:
    #
    #     # Time: O(N * logN), Space: O(N)
    #
    #     nums.sort(key=lambda x: x % 2)
    #     return nums

    # def is_even(self, num):
    #     if num % 2 == 0:
    #         return True
    #     return False
    #
    # def sortArrayByParity(self, nums: List[int]) -> List[int]:
    #
    #     # Time: O(N), Space: O(N)
    #
    #     even_array = []
    #     odd_array = []
    #     for num in nums:
    #         if self.is_even(num):
    #             even_array.append(num)
    #         else:
    #             odd_array.append(num)
    #
    #     return even_array + odd_array

    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # Time: O(N), Space: O(1)

        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] % 2 == 0:
                i += 1

            if nums[j] % 2 == 1:
                j -= 1

        return nums


if __name__ == "__main__":
    solution = Solution()

    assert solution.sortArrayByParity(nums=[3, 1, 2, 4]) == [4, 2, 1, 3]

    assert solution.sortArrayByParity(nums=[0]) == [0]
