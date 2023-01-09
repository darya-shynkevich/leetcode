# You are keeping the scores for a baseball game with strange rules. At the beginning of the game,
# you start with an empty record.
#
# You are given a list of strings operations, where operations[i] is the ith operation you must apply
# to the record and is one of the following:
#
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
#
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit
# integer and that all operations are valid.

# Constraints:
#
# 1 <= operations.length <= 1000
# operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 10^4, 3 * 10^4].
# For operation "+", there will always be at least two previous scores on the record.
# For operations "C" and "D", there will always be at least one previous score on the record.
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for operation in operations:
            if operation == "+":
                scores.append(scores[-1] + scores[-2])
            elif operation == "D":
                scores.append(2 * scores[-1])
            elif operation == "C":
                scores.pop()
            else:
                scores.append(int(operation))

        return sum(scores)


if __name__ == "__main__":
    solution = Solution()

    assert solution.calPoints(operations=["5", "2", "C", "D", "+"]) == 30

    assert solution.calPoints(operations=["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27

    assert solution.calPoints(operations=["1", "C"]) == 0
