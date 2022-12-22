# You are given an array of strings names, and an array heights that consists of distinct positive integers.
# Both arrays are of length n.
#
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
#
# Return names sorted in descending order by the people's heights.
#
# Constraints:
#
# n == names.length == heights.length
# 1 <= n <= 103
# 1 <= names[i].length <= 20
# 1 <= heights[i] <= 105
# names[i] consists of lower and upper case English letters.
# All the values of heights are distinct.
from operator import itemgetter
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_people = sorted(zip(names, heights), key=itemgetter(1), reverse=True)

        return [person[0] for person in sorted_people]


if __name__ == "__main__":
    solution = Solution()

    assert solution.sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]) == ["Mary", "Emma", "John"]

    assert solution.sortPeople(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150]) == ["Bob", "Alice", "Bob"]
