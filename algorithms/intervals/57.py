from typing import List


class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Intervals are not overlapped, but will be after inserting
        # Intervals have already been sorted
        # We will insert interval into a correct place and the merge if necessary

        intervals_len = len(intervals)
        if intervals_len == 0:
            return [newInterval]

        intervals.append(newInterval)

        intervals.sort(key=lambda interval: interval[0])

        i = 0
        while i < intervals_len:
            if intervals[i][1] >= intervals[i+1][0]:
                start = min(intervals[i][0], intervals[i+1][0])
                end = max(intervals[i][1], intervals[i+1][1])
                intervals[i], intervals[i+1] = [], [start, end]

            i += 1

        return [interval for interval in intervals if interval]


if __name__ == '__main__':
    solution = Solution()

    assert solution.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]) == [[1, 5], [6, 9]]

    assert solution.insert(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
    ) == [[1, 2], [3, 10], [12, 16]]

    assert solution.insert(intervals=[[1,5]], newInterval=[2,3]) == [[1, 5]]

    assert solution.insert(intervals=[[1,5]], newInterval=[0,0]) == [[0,0],[1,5]]

    assert solution.insert(intervals=[[1,5],[6,8]], newInterval=[3,7]) == [[1, 8]]

    assert solution.insert(intervals=[[1,5],[6,8], [9, 10]], newInterval=[3,7]) == [[1, 8], [9, 10]]
