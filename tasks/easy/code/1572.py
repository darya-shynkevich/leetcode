# Given a square matrix mat, return the sum of the matrix diagonals.
#
# Only include the sum of all the elements on the primary diagonal and all the elements
# on the secondary diagonal that are not part of the primary diagonal.

# Constraints:
#
# n == mat.length == mat[i].length
# 1 <= n <= 100
# 1 <= mat[i][j] <= 100
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        # Time: O(N), Space: O(1)

        n = len(mat)

        result = 0
        for i in range(n):
            primary_diagonal_element = mat[i][i]
            secondary_diagonal_element = mat[i][n-i-1]

            if i == n - i - 1:
                result += primary_diagonal_element
                continue

            result += (primary_diagonal_element + secondary_diagonal_element)

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.diagonalSum(mat=[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]) == 25

    assert solution.diagonalSum(mat=[
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]) == 8

    assert solution.diagonalSum(mat=[[5]]) == 5
