# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
#
# A subarray is a contiguous subsequence of the array.

# Constraints:
#
# 1 <= arr.length <= 100
# 1 <= arr[i] <= 1000

# Follow up:
#
# Could you solve this problem in O(n) time complexity?
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    assert solution.sumOddLengthSubarrays(arr=[1, 4, 2, 5, 3]) == 58

    assert solution.sumOddLengthSubarrays(arr=[1, 2]) == 3

    assert solution.sumOddLengthSubarrays(arr=[10, 11, 12]) == 66
