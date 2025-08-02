# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
#
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
#
# The test cases are generated so that a unique mapping will always exist.

# Constraints:
#
# 1 <= s.length <= 1000
# s consists of digits and the '#' letter.
# s will be a valid string such that mapping is always possible.
from string import ascii_lowercase


class Solution:
    def freqAlphabets(self, s: str) -> str:

        # Time: O(N), Space: O(N)

        n = len(s)
        i = 0

        result = []
        while i < n:
            if i + 2 < n and s[i + 2] == '#' and int(s[i:i+2]) <= 26:
                val = int(s[i:i+2])
                result.append(chr(val + 96))
                i += 3
            else:
                if s[i] != '#':
                    result.append(chr(int(s[i]) + 96))
                i += 1

        return ''.join(result)


if __name__ == "__main__":
    solution = Solution()

    assert solution.freqAlphabets(s="10#11#12") == "jkab"

    assert solution.freqAlphabets(s="1326#") == "acz"
