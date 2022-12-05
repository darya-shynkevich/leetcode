# Write a function that takes an unsigned integer and returns the number of '1' bits it has
# (also known as the Hamming weight).
#
# Note that in some languages, such as Java, there is no unsigned integer type.
# In this case, the input will be given as a signed integer type. It should not affect your implementation,
# as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation.
# Therefore, in Example 3, the input represents the signed integer. -3.

class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        while n:
            n = n & (n - 1)
            result += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.hammingWeight(n=int('00000000000000000000000000001011', 2)) == 3

    assert solution.hammingWeight(n=int('00000000000000000000000010000000', 2)) == 1

    assert solution.hammingWeight(n=int('11111111111111111111111111111101', 2)) == 31
