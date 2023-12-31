# You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
#
# Return the number of consistent strings in the array words.

# Constraints:
#
# 1 <= words.length <= 104
# 1 <= allowed.length <= 26
# 1 <= words[i].length <= 10
# The characters in allowed are distinct.
# words[i] and allowed contain only lowercase English letters.
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        # Time: O(N * M), N = len(words), M = max(len(word)), Space: O(1)

        allowed_hashmap = set()
        for char in allowed:
            allowed_hashmap.add(char)

        result = 0
        for word in words:
            is_consistent = True
            for char in word:
                if char not in allowed_hashmap:
                    is_consistent = False
                    break

            if is_consistent:
                result += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]) == 2

    assert solution.countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]) == 7

    assert solution.countConsistentStrings(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]) == 4
