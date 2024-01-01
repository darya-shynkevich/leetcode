# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    solution = Solution()
