# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
#
# A string is represented by an array if the array elements concatenated in order forms the string.

# Constraints:
#
# 1 <= word1.length, word2.length <= 103
# 1 <= word1[i].length, word2[i].length <= 103
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 103
# word1[i] and word2[i] consist of lowercase letters.
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


if __name__ == "__main__":
    solution = Solution()

    assert solution.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]) is True

    assert solution.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]) is False

    assert solution.arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]) is True
