from typing import Optional


class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False

        tail = self.reverse_list(head=self.get_medium_node(head))

        node = head
        while node and tail:
            if node.val != tail.val:
                return False

            node = node.next
            tail = tail.next

        return True

    def get_llist_len(self, head):
        node = head
        list_len = 1
        while node.next:
            list_len += 1
            node = node.next

        return list_len

    def get_medium_node(self, head):
        list_len = self.get_llist_len(head=head)

        i = 0
        node = head
        while node:
            if i == list_len // 2 - 1:
                return node.next

            node = node.next
            i += 1

    def reverse_list(self, head):
        node = head

        prev_node = None
        while node:
             next_node = node.next
             node.next = prev_node
             prev_node = node
             node = next_node

        return prev_node



if __name__ == "__main__":
    solution = Solution()

    node_4 = ListNode(next=None, x=1)
    node_3 = ListNode(next=node_4, x=2)
    node_2 = ListNode(next=node_3, x=2)
    node_1 = ListNode(next=node_2, x=1)

    assert solution.isPalindrome(head=node_1)

    solution = Solution()

    node_5 = ListNode(next=None, x=1)
    node_4 = ListNode(next=node_5, x=2)
    node_3 = ListNode(next=node_4, x=3)
    node_2 = ListNode(next=node_3, x=2)
    node_1 = ListNode(next=node_2, x=1)

    assert solution.isPalindrome(head=node_1)
