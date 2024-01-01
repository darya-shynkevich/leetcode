# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].

# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique.

# Definition for a binary tree node.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    queue = []

    result = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        self.queue.append(root)

        while self.queue:
            current_node: TreeNode = self.queue.pop()

            if current_node.left and low <= current_node.val:
                self.queue.append(current_node.left)

            if current_node.right and current_node.val <= high:
                self.queue.append(current_node.right)

            if low <= current_node.val <= high:
                self.result += current_node.val

        return self.result


if __name__ == "__main__":
    solution = Solution()

    node3 = TreeNode(3, None, None)
    node4 = TreeNode(7, None, None)
    node5 = TreeNode(18, None, None)
    node1 = TreeNode(5, node3, node4)
    node2 = TreeNode(15, None, node5)
    root = TreeNode(10, node1, node2)

    assert solution.rangeSumBST(root=root, low=7, high=15) == 32
