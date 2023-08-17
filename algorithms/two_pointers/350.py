from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == len(nums2) and nums1 == nums2:
            return nums1

        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        result = []
        i = j = 0
        while i < len(nums1) - 1:
            if nums1[i] == nums2[j]:
                result.extend([nums1[i]])
                j += 1

            i += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.intersect(nums1 = [1,2,2,1], nums2 = [2,2]) == [2, 2]

    assert solution.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]) == [4, 9]

    assert solution.intersect(nums1 = [1], nums2 = [1]) == [1]

    assert solution.intersect(nums1=[1], nums2=[1, 1]) == [1]

    assert solution.intersect(nums1=[2,1], nums2=[1, 1]) == [1]
