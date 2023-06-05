# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# 
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# 
# Change the array nums such that the first k elements of nums contain the unique elements in the order 
# they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Constraints:
# 
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.


from typing import List, Tuple


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)

        if len_nums == 0:
            return 0

        if len_nums == 1:
            return 1

        i, j = 0, 1
        while i <= j < len_nums:
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1

        return i + 1


if __name__ == "__main__":
    solution = Solution()

    assert solution.removeDuplicates(nums=[1, 1, 2]) == 2

    assert solution.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
