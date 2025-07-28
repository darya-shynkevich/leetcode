from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass



solution = Solution()

# Create first linked list: 2 -> 4 -> 3 (represents number 342)
l1 = ListNode(2, ListNode(4, ListNode(3)))

# Create second linked list: 5 -> 6 -> 4 (represents number 465)
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Expected result linked list: 7 -> 0 -> 8 (represents number 807)
result = solution.addTwoNumbers(l1, l2)
print(result)