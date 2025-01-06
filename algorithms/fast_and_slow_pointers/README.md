# Fast & Slow Pointers

The Fast & Slow Pointers (Tortoise and Hare) pattern is used to detect cycles in linked lists and other similar structures.

### Sample Problem:
Detect if a linked list has a cycle.

### Explanation:
1. Initialize two pointers, one moving one step at a time (slow) and the other moving two steps at a time (fast).
2. If there is a cycle, the fast pointer will eventually meet the slow pointer.
3. If the fast pointer reaches the end of the list, there is no cycle.

## LeetCode Problems:
1. Maximum Average Subarray I (LeetCode #643)
2. Longest Substring Without Repeating Characters (LeetCode #3)
3. Minimum Window Substring (LeetCode #76)

# References:

1. [Mastering the Art of Problem-Solving: The Sliding Window Algorithm](https://medium.com/@shadmanc/mastering-the-art-of-problem-solving-the-sliding-window-algorithm-db5ce7c2906a)
2. [Grokking the Coding Interview: Pattern Sliding Window](https://levelup.gitconnected.com/grokking-the-coding-interview-pattern-sliding-window-20ef83ae5872)
3. [Coding Interview Made Easy: Understanding the Sliding Window Pattern](https://medium.com/geekculture/coding-interview-made-easy-understanding-the-sliding-window-pattern-df907ea6f521)
4. [Leetcode Pattern 2 | Sliding Windows for Strings](https://medium.com/leetcode-patterns/leetcode-pattern-2-sliding-windows-for-strings-e19af105316b)
5. [Maximum Fruits 🍑🍒🍓🥭 Into Baskets 🧺| Coding Interview | Sliding Window Pattern](https://ganeshprasad227.medium.com/maximum-fruits-into-baskets-coding-interview-sliding-window-pattern-15fcfb1c6a86)
