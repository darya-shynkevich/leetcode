# You are given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
#
# Return the shuffled string.

# Constraints:
#
# s.length == indices.length == n
# 1 <= n <= 100
# s consists of only lowercase English letters.
# 0 <= indices[i] < n
# All values of indices are unique.

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        char_to_position_map = {key: i for i, key in enumerate(indices)}

        result = []
        for i in range(len(s)):
            result.append(s[char_to_position_map[i]])

        return ''.join(result)


if __name__ == "__main__":
    solution = Solution()

    assert solution.restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]) == "leetcode"

    assert solution.restoreString(s="abc", indices=[0, 1, 2]) == "abc"
