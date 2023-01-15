# A permutation perm of n + 1 integers of all the integers in the range [0, n]
# can be represented as a string s of length n where:
#
# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it.
# If there are multiple valid permutations perm, return any of them.

# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either 'I' or 'D'.
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        pass


if __name__ == "__main__":
    solution = Solution()

    assert solution.diStringMatch(s="IDID") == [0, 4, 1, 3, 2]

    assert solution.diStringMatch(s="III") == [0, 1, 2, 3]

    assert solution.diStringMatch(s="DDI") == [3, 2, 0, 1]
