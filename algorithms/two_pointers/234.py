from typing import Optional


class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False

        node = head
        list_len = 1
        while node.next:
            list_len += 1
            node = node.next

        tail = node

        i = 0
        medium_node, node = None, head
        while node.next:
            next_node = node.next.next
            if next_node is None:
                break

            if i >= list_len // 2 - 1:
                breakpoint()
                next_node.next = node

            node = next_node
            i += 1

        node = head
        while node:
            print(node.val, tail.val)
            if node.val != tail.val:
                return False

            node = node.next
            tail = tail.next

        return True


if __name__ == "__main__":
    solution = Solution()

    node_4 = ListNode(next=None, x=1)
    node_3 = ListNode(next=node_4, x=2)
    node_2 = ListNode(next=node_3, x=2)
    node_1 = ListNode(next=node_2, x=1)
    
    assert solution.isPalindrome(head=node_1)

    # solution = Solution()
    #
    # node_5 = ListNode(next=None, x=1)
    # node_4 = ListNode(next=node_5, x=2)
    # node_3 = ListNode(next=node_4, x=3)
    # node_2 = ListNode(next=node_3, x=2)
    # node_1 = ListNode(next=node_2, x=1)
    #
    # assert solution.isPalindrome(head=node_1)
