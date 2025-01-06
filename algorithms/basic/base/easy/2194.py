# A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:
#
# <col> denotes the column number c of the cell. It is represented by alphabetical letters.
# For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
# <row> is the row number r of the cell. The rth row is represented by the integer r.
# You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents the column c1,
# <row1> represents the row r1,
# <col2> represents the column c2, and <row2> represents the row r2, such that r1 <= r2 and c1 <= c2.
#
# Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2.
# The cells should be represented as strings in the format mentioned above and be sorted in non-decreasing
# order first by columns and then by rows.
#
# Constraints:
#
# s.length == 5
# 'A' <= s[0] <= s[3] <= 'Z'
# '1' <= s[1] <= s[4] <= '9'
# s consists of uppercase English letters, digits and ':'.

from string import ascii_uppercase
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        if not s or len(s) != 5:
            return []

        first_column = s[0]
        last_column = s[3]

        letters_range = ascii_uppercase[
            ascii_uppercase.find(first_column): ascii_uppercase.find(last_column) + 1
        ]

        first_column_index = int(s[1])
        last_column_index = int(s[4])

        result = []
        for letter in letters_range:
            result.extend(
                [
                    f"{letter}{i}"
                    for i in range(first_column_index, last_column_index + 1)
                ]
            )

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.cellsInRange(s="K1:L2") == ["K1", "K2", "L1", "L2"]

    assert solution.cellsInRange(s="A1:F1") == ["A1", "B1", "C1", "D1", "E1", "F1"]
