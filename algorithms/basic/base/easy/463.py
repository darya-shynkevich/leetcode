# You are given row x col grid representing a map where grid[i][j] = 1 represents
# land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.

# Constraints:
#
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        result = 0

        for row in range(rows):
            for colum in range(columns):
                if grid[row][colum] == 1:
                    result += 4

                    if row > 0 and grid[row - 1][colum] == 1:
                        result -= 2

                    if colum > 0 and grid[row][colum - 1] == 1:
                        result -= 2

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.islandPerimeter(grid=[
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]) == 16

    assert solution.islandPerimeter(grid=[[1]]) == 4

    assert solution.islandPerimeter(grid=[[1, 0]]) == 4
