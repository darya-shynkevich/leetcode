# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Constraints:
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

from typing import Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node: ListNode = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous


if __name__ == '__main__':
    solution = Solution()

    l5 = ListNode(5, None)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)

    solution.reverseList(head=l1)
