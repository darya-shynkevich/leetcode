# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
#
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
#
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
#
# Return the number of good triplets.

# Constraints:
#
# 3 <= arr.length <= 100
# 0 <= arr[i] <= 1000
# 0 <= a, b, c <= 1000
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_triplets_count = 0

        n = len(arr)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue

                for k in range(j + 1, n):
                    if all([
                        abs(arr[i] - arr[j]) <= a,
                        abs(arr[j] - arr[k]) <= b,
                        abs(arr[i] - arr[k]) <= c
                    ]):
                        good_triplets_count += 1

        return good_triplets_count


if __name__ == "__main__":
    solution = Solution()

    assert solution.countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3) == 4

    assert solution.countGoodTriplets(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1) == 0
