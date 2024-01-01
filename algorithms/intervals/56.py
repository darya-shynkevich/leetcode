from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Intervals are overlapping
        # 2. Sort all intervals => O(nlog(n))
        # 3. Then compare and merge

        # Time: O(nlog(n)), Space: O(1)

        intervals.sort(key=lambda interval: interval[0])

        i, intervals_len = 0, len(intervals)
        while i < intervals_len - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                start = min(intervals[i][0], intervals[i+1][0])
                end = max(intervals[i][1], intervals[i+1][1])
                merged_interval = [start, end]
                intervals[i], intervals[i + 1] = [], merged_interval

            i += 1

        return [interval for interval in intervals if interval]


if __name__ == '__main__':
    solution = Solution()

    assert solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution.merge(intervals=[[1, 4], [4, 5]]) == [[1, 5]]
