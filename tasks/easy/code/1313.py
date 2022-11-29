# We are given a list nums of integers representing a list compressed with run-length encoding.
#
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
# For each such pair, there are freq elements with value val concatenated in a sublist.
# Concatenate all the sublists from left to right to generate the decompressed list.
#
# Return the decompressed list.
#
# Constraints:
#
# 2 <= nums.length <= 100
# nums.length % 2 == 0
# 1 <= nums[i] <= 100

from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)

        result = []
        for i in range(0, nums_len - 1, 2):
            result.extend([nums[i + 1]] * nums[i])

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.decompressRLElist(nums=[1, 2, 3, 4]) == [2, 4, 4, 4]

    assert solution.decompressRLElist(nums=[1, 1, 2, 3]) == [1, 3, 3]
