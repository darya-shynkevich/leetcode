# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2,
# return the shortest distance between these two words in the list.

# Constraints:
#
# 2 <= wordsDict.length <= 3 * 10^4
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.
# word1 != word2
import math
from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        # Time: O(n), Space: O(1)

        distance = math.inf

        index_1 = index_2 = None
        for i, word in enumerate(wordsDict):

            if word == word1:
                index_1 = i
            elif word == word2:
                index_2 = i

            if index_1 is not None and index_2 is not None:
                distance = min(abs(index_2 - index_1), distance)

        return distance


if __name__ == "__main__":
    solution = Solution()

    assert solution.shortestDistance(
        wordsDict=["practice", "makes", "perfect", "coding", "makes"], word1="coding", word2="practice"
    ) == 3

    assert solution.shortestDistance(
        wordsDict=["practice", "makes", "perfect", "coding", "makes"], word1="makes", word2="coding"
    ) == 1

    assert solution.shortestDistance(wordsDict=["a", "a", "b", "b"], word1="a", word2="b") == 1
