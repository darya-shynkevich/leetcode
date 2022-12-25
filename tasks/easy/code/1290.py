# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# The most significant bit is at the head of the linked list.

# Constraints:
#
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.
from typing import List


class Solution:
    def getDecimalValue(self, head: List[int]) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    assert solution.getDecimalValue(head=[1, 0, 1]) == 5

    assert solution.getDecimalValue(head=[0]) == 0
