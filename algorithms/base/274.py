from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        len_citations = len(citations)

        if len_citations == 1:
            if citations[0] == 0:
                return 0
            return 1

        citations.sort()

        result = 0
        for i in range(len_citations):
            if citations[len_citations - 1 - i] > i:
                result += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    # 0, 1, 3, 5, 6
    assert solution.hIndex(citations=[3, 0, 6, 1, 5]) == 3

    # 1, 1, 3
    assert solution.hIndex(citations=[1, 3, 1]) == 1

    assert solution.hIndex(citations=[0, 0]) == 0

    assert solution.hIndex(citations=[0, 1]) == 1

    assert solution.hIndex(citations=[1, 2]) == 1

    assert solution.hIndex(citations=[11, 15]) == 2
