from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Tome: O(n), Space: O(1)

        if len(nums) in [0, 1]:
            return nums

        i, j = 0, 1
        while j < len(nums) and i < len(nums):

            j = max(j, i)

            if nums[j] == 0:
                j += 1
                continue

            if nums[j] != 0 and nums[i] != 0:
                i += 1
                continue

            if nums[j] != 0 and nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]

                i += 1
                j += 1

        print(nums)

        return nums


if __name__ == "__main__":
    solution = Solution()

    assert solution.moveZeroes(nums = [0,1,0,3,12]) == [1,3,12,0,0]

    assert solution.moveZeroes(nums = [0]) == [0]

    assert solution.moveZeroes(nums=[1, 2]) == [1, 2]

    assert solution.moveZeroes(nums= [1, 0, 1]) == [1, 1, 0]

    assert solution.moveZeroes(nums=[4,2,4,0,0,3,0,5,1,0]) == [4,2,4,3,5,1,0,0,0,0]
