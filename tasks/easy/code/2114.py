# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
#
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
#
# Return the maximum number of words that appear in a single sentence.

# 1 <= sentences.length <= 100
# 1 <= sentences[i].length <= 100
# sentences[i] consists only of lowercase English letters and ' ' only.
# sentences[i] does not have leading or trailing spaces.
# All the words in sentences[i] are separated by a single space.

from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        words_max = 0
        for sentence in sentences:
            words_max = max(len(sentence.split(" ")), words_max)

        return words_max


if __name__ == "__main__":
    solution = Solution()

    assert (
        solution.mostWordsFound(
            sentences=[
                "alice and bob love leetcode",
                "i think so too",
                "this is great thanks very much",
            ]
        )
        == 6
    )

    assert (
        solution.mostWordsFound(
            sentences=["please wait", "continue to fight", "continue to win"]
        )
        == 3
    )
