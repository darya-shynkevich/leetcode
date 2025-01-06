from typing import Optional


class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # Time: O(m + n), Space: O(1)

        if headA is None or headB is None:
            return None

        node_a = headA
        node_b = headB
        while node_a != node_b:
            node_a = node_a.next if node_a is not None else headB
            node_b = node_b.next if node_b is not None else headA

        return node_a


if __name__ == "__main__":
    solution = Solution()

    # List B:
    node_b_6 = ListNode(next=None, x=6)
    node_b_5 = ListNode(next=node_b_6, x=5)
    node_b_4 = ListNode(next=node_b_5, x=8)
    node_b_3 = ListNode(next=node_b_4, x=1)
    node_b_2 = ListNode(next=node_b_3, x=6)
    node_b_1 = ListNode(next=node_b_2, x=5)

    # List A:
    node_a_2 = ListNode(next=node_b_4, x=1)
    node_a_1 = ListNode(next=node_a_2, x=4)

    assert solution.getIntersectionNode(headA=node_b_1, headB=node_b_1)



