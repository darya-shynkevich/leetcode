from collections import deque


class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self, head):
        self.head = head

    def __iter__(self):
        if not self.head:
            raise

        node = self.head
        while node.next:
            yield node
            node = node.next

    def __getitem__(self, i: int):
        counter = 0

        for node in self:
            if counter == i:
                return node.data

            counter += 1

    def reverse(self):
        reversed_linked_list = deque()

        for node in self:
            reversed_linked_list.appendleft(node.data)

        return list(reversed_linked_list)

    def add_after(self, target_node: Node, new_node: Node):
        for node in self:
            if node == target_node:
                new_node.next = node.next
                node.next = new_node


if __name__ == '__main__':

    node_1 = Node(1, None)
    node_2 = Node(2, node_1)
    node_3 = Node(3, node_2)
    node_4 = Node(4, node_3)
    node_5 = Node(5, node_4)

    linked_list = LinkedList(head=node_5)

    for item in linked_list:
        print(item.data)

    print(linked_list[3])

    print(linked_list)

    print(linked_list.reverse())

    linked_list.add_after(node_4, Node(6, node_3))

    for item in linked_list:
        print(item.data)
