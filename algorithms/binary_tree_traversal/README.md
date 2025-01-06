# Binary Tree Traversal

Binary Tree Traversal involves visiting all the nodes in a binary tree in a specific order.

- PreOrder: root -> left -> right
- InOrder: left -> root -> right
- PostOrder: left -> right -> root

- ## Sample Problem:
Perform inorder traversal of a binary tree.

### Example:

- Input: root = [1, null, 2, 3]
- Output: [1, 3, 2]

### Explanation:
1. Inorder traversal visits nodes in the order: left, root, right.
2. Use recursion or a stack to traverse the tree in this order.

## LeetCode Problems:
1. PreOrder → Binary Tree Paths (LeetCode #257)
2. InOrder → Kth Smallest Element in a BST (LeetCode #230)
3. PostOrder → Binary Tree Maximum Path Sum (LeetCode #124)