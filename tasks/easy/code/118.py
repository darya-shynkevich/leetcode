# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Constraints:
#
# 1 <= numRows <= 30

from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        # Time: O(n^2), O(1)

        triangle = [[1]]

        for i in range(1, numRows):
            result_row = [0] * (i + 1)
            result_row[0] = result_row[-1] = 1

            prev_row = triangle[i - 1]
            for j in range(1, i):
                result_row[j] = prev_row[j - 1] + prev_row[j]

            triangle.append(result_row)

        return triangle


if __name__ == "__main__":
    solution = Solution()

    assert solution.generate(numRows=5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    assert solution.generate(numRows=1) == [[1]]
