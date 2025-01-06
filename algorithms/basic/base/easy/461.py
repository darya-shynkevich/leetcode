# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, return the Hamming distance between them.
#
# Constraints:
#
# 0 <= x, y <= 2^31 - 1


class Solution:
    def hammingDistance(self, x, y):
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            xor = xor & (xor - 1)  # remove the rightmost bit of '1'

        return distance


if __name__ == "__main__":
    solution = Solution()

    assert solution.hammingDistance(x=1, y=4) == 2

    assert solution.hammingDistance(x=3, y=1) == 1
