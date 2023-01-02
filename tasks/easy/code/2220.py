# A bit flip of a number x is choosing a bit in the binary representation
# of x and flipping it from either 0 to 1 or 1 to 0.
#
# For example, for x = 7, the binary representation is 111 and we may choose any bit
# (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110,
# flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
# Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

# Constraints:
#
# 0 <= start, goal <= 109


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        # Time O(log(n)), Space O(1)

        xor = start ^ goal
        distance = 0
        while xor:
            distance += 1
            xor = xor & (xor - 1)  # remove the rightmost bit of '1'

        return distance


if __name__ == "__main__":
    solution = Solution()

    assert solution.minBitFlips(start=10, goal=7) == 3

    assert solution.minBitFlips(start=3, goal=4) == 3
