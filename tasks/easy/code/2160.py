# You are given a positive integer num consisting of exactly four digits.
# Split num into two new integers new1 and new2 by using the digits found in num.
# Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.
#
# For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3.
# Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
# Return the minimum possible sum of new1 and new2.

from itertools import combinations, permutations


class Solution:
    def minimumSum(self, num: int) -> int:

        min_sum = num
        for combination in list(permutations(str(num))):
            number_1 = int(f"{combination[0]}{combination[1]}")
            number_2 = int(f"{combination[2]}{combination[3]}")
            min_sum = min(number_1 + number_2, min_sum)

            number_1 = int(f"{combination[0]}{combination[1]}{combination[2]}")
            number_2 = int(f"{combination[3]}")
            min_sum = min(number_1 + number_2, min_sum)

        return min_sum


if __name__ == "__main__":
    solution = Solution()

    assert solution.minimumSum(num=2932) == 52

    assert solution.minimumSum(num=4009) == 13

    assert solution.minimumSum(num=1000) == 1
