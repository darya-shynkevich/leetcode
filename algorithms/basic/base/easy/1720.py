# There is a hidden integer array arr that consists of n non-negative integers.
#
# It was encoded into another integer array encoded of length n - 1,
# such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].
#
# You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].
#
# Return the original array arr. It can be proved that the answer exists and is unique.
#
# Constraints:
#
# 2 <= n <= 104
# encoded.length == n - 1
# 0 <= encoded[i] <= 105
# 0 <= first <= 105

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]

        for i, number in enumerate(encoded):
            decoded.append(decoded[i] ^ encoded[i])

        return decoded


if __name__ == "__main__":
    solution = Solution()

    assert solution.decode(encoded=[1, 2, 3], first=1) == [1, 0, 2, 1]

    assert solution.decode(encoded=[6, 2, 7, 3], first=4) == [4, 2, 0, 7, 4]
