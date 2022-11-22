# There is a programming language with only four operations and one variable X:
#
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
#
# Given an array of strings operations containing a list of operations,
# return the final value of X after performing all the operations.

# 1 <= operations.length <= 100
# operations[i] will be either "++X", "X++", "--X", or "X--".

from typing import List


class Solution:

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for operation in operations:
            if "+" in operation:
                x += 1
            else:
                x -= 1

        return x


if __name__ == "__main__":
    solution = Solution()

    assert solution.finalValueAfterOperations(operations=["--X", "X++", "X++"]) == 1

    assert solution.finalValueAfterOperations(operations=["++X", "++X", "X++"]) == 3

    assert solution.finalValueAfterOperations(operations=["X++", "++X", "--X", "X--"]) == 0
