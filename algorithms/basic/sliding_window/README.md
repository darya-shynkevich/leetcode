# Sliding Window

The Sliding Window pattern is used to find a subarray or substring that satisfies a specific condition, optimizing the time complexity by maintaining a window of elements.

Use this pattern when dealing with problems involving contiguous subarrays or substrings.

### Sample Problem:
Find the maximum sum of a subarray of size k.

### Example:

- Input: nums = [2, 1, 5, 1, 3, 2], k = 3
- Output: 9

### Explanation:
1. Start with the sum of the first k elements.
2. Slide the window one element at a time, subtracting the element that goes out of the window and adding the new element.
3. Keep track of the maximum sum encountered.

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
