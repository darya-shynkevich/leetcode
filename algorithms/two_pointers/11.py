from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        len_height = len(height)

        if len_height in [0, 1]:
            return 0

        i, j = 0, len_height - 1
        max_area, current_max_height = 0, 0
        while i < j:
            current_area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, current_area)

            # print(i, j, height[i], height[j], current_area, max_area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    assert solution.maxArea(height=[1, 1]) == 1

    assert solution.maxArea(height=[2, 3, 4, 5, 18, 17, 6]) == 17

    assert solution.maxArea(height=[5, 3, 2, 5, 25, 24, 5]) == 30

    assert solution.maxArea(height=[1, 3, 2, 5, 25, 24, 5]) == 24
