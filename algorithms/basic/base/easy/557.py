# Given a string s, reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.

# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])[::-1]


if __name__ == "__main__":
    solution = Solution()

    s = "Let's take LeetCode contest"

    assert solution.reverseWords(s=s) == "s'teL ekat edoCteeL tsetnoc"

    s = "God Ding"

    assert solution.reverseWords(s=s) == "doG gniD"
