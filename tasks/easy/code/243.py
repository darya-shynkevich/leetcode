# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2,
# return the shortest distance between these two words in the list.

# Constraints:
#
# 2 <= wordsDict.length <= 3 * 104
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.
# word1 != word2
from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    assert solution.shortestDistance(
        wordsDict=["practice", "makes", "perfect", "coding", "makes"], word1="coding", word2="practice"
    ) == 3

    assert solution.shortestDistance(
        wordsDict=["practice", "makes", "perfect", "coding", "makes"], word1="makes", word2="coding"
    ) == 1

