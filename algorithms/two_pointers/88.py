# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function,
# but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Constraints:
#
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109

# Follow-up: Can you come up with an algorithm that runs in O(m + n) time?

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m == 0:
            nums1 = nums2
            return nums1

        if m + n == 1:
            nums1 = nums1 or nums2
            return nums1

        i = j = 0

        while i < n + m and j < n:

            if nums2[j] < nums1[i]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
            elif nums1[i] == 0:
                nums1[i] = nums2[j]
                j += 1
            else:
                i += 1

        return nums1


if __name__ == "__main__":
    solution = Solution()

    assert solution.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) == [1, 2, 2, 3, 5, 6]

    assert solution.merge(nums1=[1, 2, 2, 3, 5, 0, 0, 0], m=5, nums2=[2, 5, 6], n=3) == [1, 2, 2, 2, 3, 5, 5, 6]

    assert solution.merge(nums1=[1], m=1, nums2=[], n=0) == [1]

    assert solution.merge(nums1=[0], m=0, nums2=[1], n=1) == [1]
