# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# Each of the words consists of only uppercase and lowercase English letters (no punctuation).
#
# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.

# Constraints:
#
# 1 <= s.length <= 500
# k is in the range [1, the number of words in s].
# s consist of only lowercase and uppercase English letters and spaces.
# The words in s are separated by a single space.
# There are no leading or trailing spaces.


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        pass


if __name__ == "__main__":
    solution = Solution()

    assert solution.truncateSentence(s="Hello how are you Contestant", k=4) == "Hello how are you"

    assert solution.truncateSentence(s="What is the solution to this problem", k=4) == "What is the solution"

    assert solution.truncateSentence(s="chopper is not a tanuki", k=5) == "chopper is not a tanuki"
