# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram,
# or false otherwise.

# Constraints:
#
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.
from string import ascii_lowercase


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(ascii_lowercase) == len(set(sentence))


if __name__ == "__main__":
    solution = Solution()

    assert solution.checkIfPangram(sentence="thequickbrownfoxjumpsoverthelazydog") is True

    assert solution.checkIfPangram(sentence="leetcode") is False
