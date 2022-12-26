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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num


if __name__ == "__main__":
    solution = Solution()

    n3 = ListNode(val=1, next=None)
    n2 = ListNode(val=0, next=n3)
    n1 = ListNode(val=1, next=n2)
    assert solution.getDecimalValue(head=n1) == 5

    solution = Solution()
    n1 = ListNode(val=0, next=None)
    assert solution.getDecimalValue(head=n1) == 0
