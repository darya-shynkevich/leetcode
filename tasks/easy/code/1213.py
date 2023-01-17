# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order,
# return a sorted array of only the integers that appeared in all three arrays.

# Constraints:
#
# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000
import collections
from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

        # Time: O(min(len(arr1), len(arr2), len(arr3)), Space: O(N)

        return list(set(arr1) & set(arr2) & set(arr3))

    # def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    #
    #     # Time: O(N), Space: O(N)
    #
    #     counter = collections.Counter(arr1 + arr2 + arr3)
    #
    #     result = []
    #
    #     for item in counter:
    #         if counter[item] == 3:
    #             result.append(item)
    #     return result

    # def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    #
    #     # Time: O(N), Space: O(1)
    #
    #     result = []
    #
    #     p1 = p2 = p3 = 0
    #     while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
    #         if arr1[p1] == arr2[p2] == arr3[p3]:
    #             result.append(arr1[p1])
    #             p1 += 1
    #             p2 += 1
    #             p3 += 1
    #         else:
    #             if arr1[p1] < arr2[p2]:
    #                 p1 += 1
    #             elif arr2[p2] < arr3[p3]:
    #                 p2 += 1
    #             else:
    #                 p3 += 1
    #
    #     return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.arraysIntersection(arr1=[1, 2, 3, 4, 5], arr2=[1, 2, 5, 7, 9], arr3=[1, 3, 4, 5, 8]) == [1, 5]

    assert solution.arraysIntersection(
        arr1=[197, 418, 523, 876, 1356], arr2=[501, 880, 1593, 1710, 1870], arr3=[521, 682, 1337, 1395, 1764]
    ) == []
