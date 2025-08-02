# Given an array of strings patterns and a string word, return the number of strings
# in patterns that exist as a substring in word.
#
# A substring is a contiguous sequence of characters within a string.

# Constraints:
#
# 1 <= patterns.length <= 100
# 1 <= patterns[i].length <= 100
# 1 <= word.length <= 100
# patterns[i] and word consist of lowercase English letters.
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:

        # Time: O(N * M), Space: O(1)

        result = 0
        word_len = len(word)
        for pattern in patterns:
            if len(pattern) > word_len:
                continue

            if pattern in word:
                result += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.numOfStrings(patterns=["a", "abc", "bc", "d"], word="abc") == 3

    assert solution.numOfStrings(patterns=["a", "b", "c"], word="aaaaabbbbb") == 2

    assert solution.numOfStrings(patterns=["a", "a", "a"], word="ab") == 3
