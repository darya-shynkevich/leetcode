from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) in [0, 1]:
            return 0

        min_price, max_profit = inf, 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif max_profit < price - min_price:
                max_profit = price - min_price

        return max_profit


if __name__ == '__main__':
    solution = Solution()

    assert solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5

    assert solution.maxProfit(prices=[7, 6, 4, 3, 1]) == 0

    assert solution.maxProfit(prices=[7, 1, 5, 3, 60, 4]) == 59

    assert solution.maxProfit(prices=[2, 4, 1]) == 2

    assert solution.maxProfit(prices=[2, 4, 1, 7, 2, 10]) == 9

    assert solution.maxProfit(prices=[2, 1, 4]) == 3
