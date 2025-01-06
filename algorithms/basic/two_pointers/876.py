from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:

    def get_list_len(self, head: Optional[ListNode]) -> int:

        node = head

        list_len = 0
        while node:
            list_len += 1
            node = node.next

        return list_len


    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # T: O(n), S: O(1)

        if head is None:
            return None

        if head.next is None:
            return head

        list_len = self.get_list_len(head=head)

        middle_node = list_len // 2

        node = head

        i = 0
        while node and i != middle_node:
            node = node.next
            i += 1

        return node


if __name__ == "__main__":
    solution = Solution()

    node_5 = ListNode(next=None, val=4)
    node_4 = ListNode(next=node_5, val=4)
    node_3 = ListNode(next=node_4, val=3)
    node_2 = ListNode(next=node_3, val=2)
    node_1 = ListNode(next=node_2, val=1)

    assert solution.middleNode(head=node_1) == node_3

    solution = Solution()

    node_4 = ListNode(next=None, val=4)
    node_3 = ListNode(next=node_4, val=3)
    node_2 = ListNode(next=node_3, val=2)
    node_1 = ListNode(next=node_2, val=1)

    assert solution.middleNode(head=node_1) == node_3

    solution = Solution()

    assert solution.middleNode(head=None) is None

    solution = Solution()

    node_1 = ListNode(next=None, val=1)

    assert solution.middleNode(head=node_1) == node_1
