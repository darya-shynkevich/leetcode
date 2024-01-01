# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
#
# 1 <= s.length <= 100
# s consists of printable ASCII characters.

from string import ascii_uppercase


class Solution:
    def toLowerCase(self, s: str) -> str:
        s_map = {value for value in s}

        for char in ascii_uppercase:
            if char in s_map:
                s = s.replace(char, char.lower())

        return s


if __name__ == "__main__":
    solution = Solution()

    assert solution.toLowerCase(s="Hello") == "hello"

    assert solution.toLowerCase(s="here") == "here"

    assert solution.toLowerCase(s="LOVELY") == "lovely"
