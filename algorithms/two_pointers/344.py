# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.

# 1 <= s.length <= 105
# s[i] is a printable ascii character.
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len_s = len(s)

        for i in range(len_s):
            if i == j - i - 1 or j - i - 1 == 0:
                break

            s[i], s[j - i - 1] = s[j - i - 1], s[i]

        self.s = s


if __name__ == "__main__":
    solution = Solution()

    solution.reverseString(s=["h", "e", "l", "l", "o"])
    assert solution.s == ["o", "l", "l", "e", "h"]

    solution.reverseString(s=["H", "a", "n", "n", "a", "h"])
    assert solution.s == ["h", "a", "n", "n", "a", "H"]
