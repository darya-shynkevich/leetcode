from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights_len = len(heights)

        if heights_len == 0:
            return 0

        if heights_len == 1:
            return heights[0]

        heights.append(0)
        stack = [-1]
        max_area = 0
        for i in range(heights_len + 1):
            while heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        heights.pop()
        return max_area


solution = Solution()
assert solution.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]) == 10
assert solution.largestRectangleArea(heights=[2, 4]) == 4



