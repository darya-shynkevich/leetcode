# Monotonic Stack

A monotonic stack is a stack whose elements are monotonically increasing or descreasing.

Monotonic stack is a stack with the guarantee of monotonicity for stack elements, 
which is more strictly limited than a normal stack. 
It requires that every element pushed onto the stack must be sorted 
(if the new element pushed does not meet the requirement, 
the previous elements will be popped out of the stack until the requirement is met before pushing the new element), 
forming a monotonic increasing or decreasing stack.


## Increasing or decreasing?
If we need to pop smaller elements from the stack before pushing a new element, the stack is decreasing from bottom to top.
Otherwise, it's increasing from bottom to top.

**For example, Mono-decreasing Stack:**

1. Before: [5,4,2,1] 
2. To push 3, we need to pop smaller (or equal) elements first 
3. After: [5,4,3]

# References:
1. [Monotonic Stack + List of problems on Leetcode](!https://liuzhenglaichn.gitbook.io/algorithm/monotonic-stack)
2. [Introduction to monotonic stack that everyone can understand](!https://medium.com/@florian_algo/introduction-to-monotonic-stack-that-everyone-can-understand-e5f54467faaf)
3. [Monotonic Stack — Identify Pattern](!https://itnext.io/monotonic-stack-identify-pattern-3da2d491a61e)