from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Intervals are 1. not overlapped and 2. sorted
        if len(firstList) == 0 or len(secondList) == 0:
            return []

        i, j = 0, 0
        result = []
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                result.append([start, end])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert solution.intervalIntersection(
        firstList=[[0, 2], [5, 10], [13, 23], [24, 25]], secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]
    ) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    assert solution.intervalIntersection(firstList=[[1, 3], [5, 9]], secondList=[]) == []

    assert solution.intervalIntersection(firstList=[[1, 3]], secondList=[[5, 9]]) == []

    assert solution.intervalIntersection(firstList=[[1, 7]], secondList=[[3, 10]]) == [[3, 7]]
