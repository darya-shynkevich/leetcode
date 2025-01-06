# You are given a 0-indexed string s that has lowercase English letters in its
# even indices and digits in its odd indices.
#
# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.
#
# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).
#
# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

# Constraints:
#
# 1 <= s.length <= 100
# s consists only of lowercase English letters and digits.
# shift(s[i-1], s[i]) <= 'z' for all odd indices i.
from string import ascii_lowercase


class Solution:
    def replaceDigits(self, s: str) -> str:

        # Time: O(N), Space: O(N)

        letter_to_next = {}
        for i in range(len(ascii_lowercase)):
            letter_to_next.update({ord(ascii_lowercase[i]): ascii_lowercase[i]})

        result = []
        prev_element = None
        for element in s:
            if not element.isnumeric():
                prev_element = element
                result.append(element)
            else:
                result.append(letter_to_next.get(ord(prev_element) + int(element)))

        return ''.join(result)


if __name__ == "__main__":
    solution = Solution()

    assert solution.replaceDigits(s="a1c1e1") == "abcdef"

    assert solution.replaceDigits(s="a1b2c3d4e") == "abbdcfdhe"
