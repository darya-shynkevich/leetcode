from typing import List


class Solution:

    # T: O(n), Memory: O(1)

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        current_index = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[current_index - 2]:
                nums[current_index] = nums[i]
                current_index += 1

        return current_index


if __name__ == '__main__':
    solution = Solution()

    assert solution.removeDuplicates(nums=[1, 1, 1, 2, 2, 3, 3, 3]) == 6

    assert solution.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7
