# Given an array of strings words, return the words that can be typed using letters
# of the alphabet on only one row of American keyboard like the image below.
#
# In the American keyboard:
#
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# Constraints:
#
# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase).
from typing import List


class Solution:
    FIRST = {'q', 'w', 'e', 't', 'y', 'u', 'i', 'o', 'p', 'r'}

    SECOND = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}

    THIRD = {'z', 'x', 'c', 'v', 'b', 'n', 'm', }

    def findWords(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            word_set = set(word.lower())
            if word_set.issubset(self.FIRST) or word_set.issubset(self.SECOND) or word_set.issubset(self.THIRD):
                result.append(word)

        return result


if __name__ == "__main__":
    solution = Solution()

    # assert solution.findWords(words=["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
    #
    # assert solution.findWords(words=["omk"]) == []
    #
    # assert solution.findWords(words=["adsdf", "sfd"]) == ["adsdf", "sfd"]

    assert solution.findWords(words=["qwertyuiop"]) == ["qwertyuiop"]
