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

    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #
    #     # Time: O(mn), Space: O(1)
    #
    #     if m + n == 1:
    #         nums1[0] = nums1[0] or nums2[0]
    #         return nums1
    #
    #     if not nums1 or not nums2:
    #         nums1 = nums2 or nums1[:m]
    #         return nums2 or nums1[:m]
    #
    #     for i in range(m + n):
    #         if i >= m:
    #             nums1[i:] = nums2
    #             return nums1
    #
    #         if nums1[i] > nums2[0]:
    #             nums1[i], nums2[0] = nums2[0], nums1[i]
    #
    #             k = 0
    #             while k < n - 1 and nums2[k] > nums2[k + 1]:
    #                 nums2[k], nums2[k + 1] = nums2[k + 1], nums2[k]
    #                 k += 1
    #
    #     return nums1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Follow-up, Time: O(m + n)

        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

        return nums1


if __name__ == "__main__":
    solution = Solution()

    assert solution.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) == [1, 2, 2, 3, 5, 6]

    assert solution.merge(nums1=[1, 2, 2, 3, 5, 0, 0, 0], m=5, nums2=[2, 5, 6], n=3) == [1, 2, 2, 2, 3, 5, 5, 6]

    assert solution.merge(nums1=[1], m=1, nums2=[], n=0) == [1]

    assert solution.merge(nums1=[0], m=0, nums2=[1], n=1) == [1]

    assert solution.merge(nums1=[4, 5, 6, 0, 0, 0], m=3, nums2=[1, 2, 3], n=3) == [1, 2, 3, 4, 5, 6]

    assert solution.merge(nums1=[1,2,3,4,5], m=5, nums2=[], n=0) == [1,2,3,4,5]

    assert solution.merge(nums1=[-1,0,0,3,3,3,0,0,0], m=6, nums2=[1,2,2], n=3) == [-1, 0, 0, 1, 2, 2, 3, 3, 3]

