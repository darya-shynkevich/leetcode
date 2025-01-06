# Binary Search

## Modified Binary Search
The Modified Binary Search pattern adapts binary search to solve a wider range of problems, such as finding elements in rotated sorted arrays.

Use this pattern for problems involving sorted or rotated arrays where you need to find a specific element.

### Sample Problem:
Find an element in a rotated sorted array.

#### Example:

- Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
- Output: 4

#### Explanation:
1. Perform binary search with an additional check to determine which half of the array is sorted.
2. We then check if the target is within the range of the sorted half.
3. If it is, we search that half; otherwise, we search the other half.

### LeetCode Problems:
1. Search in Rotated Sorted Array (LeetCode #33)
2. Find Minimum in Rotated Sorted Array (LeetCode #153)
3. Search a 2D Matrix II (LeetCode #240)


# References:

1. [[Python] Powerful Ultimate Binary Search Template. Solved many problems](https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)
2. [Binary Search (video)](https://www.youtube.com/watch?v=D5SrAga1pno)
3. [Binary Search (video)](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)
4. [Binary search](https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/)
5. [Demystifying Depth-First Search](https://medium.com/basecs/demystifying-depth-first-search-a7c14cccf056)
6. [Breaking Down Breadth-First Search](https://medium.com/basecs/breaking-down-breadth-first-search-cebe696709d9)
7. [Algorithms Series' Articles (at the end)](https://dev.to/jamesrweb/series/4401)
8. [How to Do a Binary Search in Python](https://realpython.com/binary-search-python/)
9. [Поиск в глубину, поиск в ширину, алгоритмы Дейкстры и А* — это один и тот же алгоритм](https://habr.com/ru/companies/yandex_praktikum/articles/705178/)
10. [Красивый двоичный поиск без ветвления](https://habr.com/ru/articles/732632/)
