# There are n kids with candies. You are given an integer array candies,
# where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies,
# denoting the number of extra candies that you have.
#
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
# they will have the greatest number of candies among all the kids, or false otherwise.
#
# Note that multiple kids can have the greatest number of candies.
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        potential_maxes = max(candies) - extraCandies

        result = []
        for candy in candies:
            result.append(True if candy >= potential_maxes else False)

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3) == [True, True, True, False, True]

    assert solution.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1) == [True, False, False, False, False]

    assert solution.kidsWithCandies(candies=[12, 1, 12], extraCandies=10) == [True, False, True]
