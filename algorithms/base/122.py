from typing import List


class Solution:

    # T: O(n), Memory: O(1)

    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                result += prices[i] - prices[i - 1]

        return result


if __name__ == '__main__':
    solution = Solution()

    assert solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 7

    assert solution.maxProfit(prices=[7, 1, 2, 5, 3, 6, 4]) == 7

    assert solution.maxProfit(prices=[1, 2, 3, 4, 5]) == 4
