# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s, split it into some number of substrings such that:
#
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.


class Solution:

    def balancedStringSplit(self, s: str) -> int:
        result = 0

        if not s or len(s) == 0:
            return result

        l_count = 0
        r_count = 0

        for char in s:
            if char == 'L':
                l_count += 1
            else:
                r_count += 1

            if l_count == r_count:
                result += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.balancedStringSplit(s="RLRRLLRLRL") == 4

    assert solution.balancedStringSplit(s="RLRRRLLRLL") == 2

    assert solution.balancedStringSplit(s="RL") == 1
