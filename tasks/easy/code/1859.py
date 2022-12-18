# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# Each word consists of lowercase and uppercase English letters.
#
# A sentence can be shuffled by appending
# the 1-indexed word position to each word then rearranging the words in the sentence.
#
# For example, the sentence
# "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

# Constraints:
#
# 2 <= s.length <= 200
# s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
# The number of words in s is between 1 and 9.
# The words in s are separated by a single space.
# s contains no leading or trailing spaces.


class Solution:
    def sortSentence(self, s: str) -> str:

        # Time: O(len(s)), Space: O(len(s))

        words = s.split(' ')

        result = [None] * len(words)
        for word in words:
            place = int(word[-1]) - 1
            result[place] = word[:-1]

        return ' '.join(result)


if __name__ == "__main__":
    solution = Solution()

    assert solution.sortSentence("is2 sentence4 This1 a3") == "This is a sentence"

    assert solution.sortSentence("Myself2 Me1 I4 and3") == "Me Myself and I"
