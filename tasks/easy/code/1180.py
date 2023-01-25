# Given a string s, return the number of substrings that have only one distinct letter.

# Constraints:
#
# 1 <= s.length <= 1000
# s[i] consists of only lowercase English letters.

class Solution:
    def countLetters(self, s: str) -> int:
        total = 1
        substrings = [0] * len(s)
        substrings[0] = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                substrings[i] = substrings[i-1] + 1
            else:
                substrings[i] = 1
            total += substrings[i]
        return total


if __name__ == "__main__":
    solution = Solution()

    assert solution.countLetters(s="aaaba") == 8

    assert solution.countLetters(s="aaaaaaaaaa") == 55
