# Matrix Traversal

Matrix Traversal involves traversing elements in a matrix using different techniques (DFS, BFS, etc.).

Use this pattern for problems involving traversing 2D grids or matrices horizontally, vertically or diagonally.

## Sample Problem:
Perform flood fill on a 2D grid. Change all the cells connected to the starting cell to new color.

### Example:

- Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
- Output: [[2,2,2],[2,2,0],[2,0,1]]

### Explanation:
1. Use DFS or BFS to traverse the matrix starting from the given cell.
2. Change the color of the connected cells to the new color.

## LeetCode Problems:
1. Flood Fill (LeetCode #733)
2. Number of Islands (LeetCode #200)
3. Surrounded Regions (LeetCode #130)