# You are given an n x n integer matrix grid.
#
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
#
# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
#
# Return the generated matrix.

# Constraints:
#
# n == grid.length == grid[i].length
# 3 <= n <= 100
# 1 <= grid[i][j] <= 100
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        # Time: O(n^2), Space: O(1)

        n = len(grid)
        result = [[0]*(n-2) for _ in range(n-2)]

        for i in range(n - 2):
            for j in range(n - 2):
                result[i][j] = max(grid[ii][jj] for ii in range(i, i+3) for jj in range(j, j+3))

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.largestLocal(grid=[
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2]
    ]) == [[9, 9], [8, 6]]

    assert solution.largestLocal(
        grid=[
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
    ) == [
        [2, 2, 2],
        [2, 2, 2],
        [2, 2, 2]
    ]
