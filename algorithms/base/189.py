from typing import List


class Solution:

    # T: O(n), Memory O(1)

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        step = k % len(nums)

        nums[:] = nums[-step:] + nums[:-step]

        return nums


if __name__ == '__main__':
    solution = Solution()

    assert solution.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3) == [5, 6, 7, 1, 2, 3, 4]

    assert solution.rotate(nums=[1, 2], k=3) == [2, 1]

    assert solution.rotate(nums=[1, 2, 3], k=4) == [3, 1, 2]
