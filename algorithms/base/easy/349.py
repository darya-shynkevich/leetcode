# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.
#
# Constraints:
#
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Time: O(n + m), Space: O(n + m)

        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set & nums2_set)


if __name__ == "__main__":
    solution = Solution()

    assert solution.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]) == [2]

    assert solution.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]) == [9, 4]
