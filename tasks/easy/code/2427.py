# Given two positive integers a and b, return the number of common factors of a and b.
#
# An integer x is a common factor of a and b if x divides both a and b.

# Constraints:
#
# 1 <= a, b <= 1000

class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        # Time: O(min(a,b)), Space: O(1)

        result = 0
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                result += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.commonFactors(a=12, b=6) == 4

    assert solution.commonFactors(a=25, b=30) == 2
