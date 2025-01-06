# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# 1 <= n <= 500
# nums.length == 2n
# 1 <= nums[i] <= 10^3

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.extend([nums[i], nums[n + i]])

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.shuffle(nums=[2, 5, 1, 3, 4, 7], n=3) == [2, 3, 5, 4, 1, 7]

    assert solution.shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4) == [1, 4, 2, 3, 3, 2, 4, 1]

    assert solution.shuffle(nums=[1, 1, 2, 2], n=2) == [1, 2, 1, 2]
