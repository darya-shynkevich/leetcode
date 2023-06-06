# Finding cycle in Linked list

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def solution(head: ListNode) -> bool:
    if not head or not head.next:
        return False

    p1 = head
    p2 = head.next

    while p2:
        p2 = p2.next

        if not p2:
            return False

        p2 = p2.next

        if p1 == p2:
            return True

        p1 = p1.next


if __name__ == "__main__":
    linked_list = [ListNode(item) for item in [3, 2, 0, -4]]

    head = linked_list[0]
    head.next = linked_list[1]
    linked_list[1].next = linked_list[2]
    linked_list[2].next = linked_list[3]
    linked_list[3].next = linked_list[1]

    assert solution(head) is True

    linked_list = [ListNode(item) for item in [3, 2, 0, -4]]

    head = linked_list[0]
    head.next = linked_list[1]
    linked_list[1].next = linked_list[2]
    linked_list[2].next = linked_list[3]
    linked_list[3].next = None

    assert solution(head) is False

    linked_list = [ListNode(item) for item in [1, 2]]

    head = linked_list[0]
    head.next = linked_list[1]
    linked_list[1].next = head

    assert solution(head) is True

    linked_list = [ListNode(item) for item in [3, 2, 0, -4]]

    head = linked_list[0]
    head.next = linked_list[1]
    linked_list[1].next = linked_list[2]
    linked_list[2].next = linked_list[3]
    linked_list[3].next = linked_list[0]

    assert solution(head) is True
