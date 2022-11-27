# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

# Constraints: 1 <= n <= 10^5

class Solution:  # Time: O(log(n)), Space: O(1)

    def subtractProductAndSum(self, n: int) -> int:
        if n == 0: return 1

        n_product = 1
        n_sum = 0

        while n:
            digit: int = n % 10
            n_product = n_product * digit
            n_sum = n_sum + digit
            n = n // 10

        return n_product - n_sum


if __name__ == "__main__":
    solution = Solution()

    assert solution.subtractProductAndSum(n=234) == 15

    assert solution.subtractProductAndSum(n=4421) == 21
