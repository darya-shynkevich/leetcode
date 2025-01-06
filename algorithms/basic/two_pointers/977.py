import collections
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Time: O(n), Space: O(n)
        # To reduce space to O(1) use result = [] and append() method

        result = collections.deque()

        i, j = 0, len(nums) - 1
        while i <= j:
            nums_j = nums[j] ** 2
            nums_i = nums[i] ** 2

            if nums_j > nums_i:
                result.appendleft(nums_j)
                j -= 1
            else:
                result.appendleft(nums_i)
                i += 1

        return list(result)


if __name__ == "__main__":
    solution = Solution()

    assert solution.sortedSquares(nums = [-4,-1,0,3,10]) == [0,1,9,16,100]

    assert solution.sortedSquares(nums = [-7,-3,2,3,11]) == [4,9,9,49,121]
