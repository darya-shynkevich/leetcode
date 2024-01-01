# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the
# i^(th) customer has in the j^(th) bank.
# Return the wealth that the richest customer has.
#
# A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.

# m == accounts.length
# n == accounts[i].length
# 1 <= m, n <= 50
# 1 <= accounts[i][j] <= 100

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0

        for account in accounts:
            max_sum = max(max_sum, sum(account))

        return max_sum


if __name__ == "__main__":
    solution = Solution()

    assert solution.maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]]) == 10

    assert solution.maximumWealth(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17

    assert solution.maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]) == 6
