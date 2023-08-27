from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        # Time: O(min(n, m)), Space: O(1)

        i = j = 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:
                return nums1[i]

            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    assert solution.getCommon(nums1 = [1,2,3], nums2 = [2,4]) == 2

    assert solution.getCommon(nums1 = [1,2,3,6], nums2 = [2,3,4,5]) == 2

    assert solution.getCommon(nums1 = [1,2], nums2 = [2, 4]) == 2
