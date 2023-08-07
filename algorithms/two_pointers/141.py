from typing import Optional


class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Time: O(n), Space: O(1)

        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True

if __name__ == "__main__":
    solution = Solution()

    node_4 = ListNode(x=-4)
    node_3 = ListNode(next=node_4, x=0)
    node_2 = ListNode(next=node_3, x=2)
    node_1 = ListNode(next=node_2, x=3)

    node_4.next = node_2

    assert solution.hasCycle(head=node_1)

    node_2 = ListNode(x=2)
    node_1 = ListNode(next=node_2, x=1)

    node_2.next = node_1

    assert solution.hasCycle(head=node_1)

    node_1 = ListNode(next=None, x=3)

    assert solution.hasCycle(head=node_1) is False
