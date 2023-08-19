from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # T: O(n + m), S: O(n)

        if len(nums1) == len(nums2) and nums1 == nums2:
            return nums1

        hash_map1 = defaultdict(int)
        for num in nums1:
            hash_map1[num] += 1

        result = []
        for num in nums2:
            if num in hash_map1 and hash_map1[num] > 0:
                result.append(num)
                hash_map1[num] -= 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.intersect(nums1 = [1,2,2,1], nums2 = [2,2]) == [2, 2]

    assert solution.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]) == [9, 4]

    assert solution.intersect(nums1 = [1], nums2 = [1]) == [1]

    assert solution.intersect(nums1=[1], nums2=[1, 1]) == [1]

    assert solution.intersect(nums1=[2,1], nums2=[1, 1]) == [1]
