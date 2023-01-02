# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair.
# In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
#
# Return the number of '*' in s, excluding the '*' between each pair of '|'.
#
# Note that each '|' will belong to exactly one pair.

# Constraints:
#
# 1 <= s.length <= 1000
# s consists of lowercase English letters, vertical bars '|', and asterisks '*'.
# s contains an even number of vertical bars '|'.


class Solution:
    def countAsterisks(self, s: str) -> int:
        result = 0

        inside_pair = False
        for char in s:
            if char == '|':
                inside_pair = not inside_pair
                continue

            if inside_pair:
                continue

            if char == '*':
                result += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.countAsterisks(s="l|*e*et|c**o|*de|") == 2

    assert solution.countAsterisks(s="iamprogrammer") == 0

    assert solution.countAsterisks(s="yo|uar|e**|b|e***au|tifu|l") == 5
