# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Constraints:
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

from typing import Optional


class ListNode:  # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:  # 1. Iterative (O(n) Time / O(1) Space)
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         previous_node: Optional[ListNode] = None
#         current_node: ListNode = head
#
#         while current_node:
#             next_node: ListNode = current_node.next
#             current_node.next = previous_node
#
#             previous_node = current_node
#             current_node = next_node
#
#         return previous_node


class Solution:  # 2. Recursive (O(n) Time / O(n) Space)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        result = self.reverseList(head=head.next)

        next_node: ListNode = head.next

        next_node.next = head
        head.next = None

        return result


if __name__ == "__main__":
    solution = Solution()

    l5 = ListNode(5, None)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)

    solution.reverseList(head=l1)
