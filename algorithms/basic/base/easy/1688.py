# You are given an integer n, the number of teams in a tournament that has strange rules:
#
# If the current number of teams is even, each team gets paired with another team.
# A total of n / 2 matches are played, and n / 2 teams advance to the next round.
# If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired.
# A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
# Return the number of matches played in the tournament until a winner is decided.

# Constraints:
#
# 1 <= n <= 200

class Solution:
    def numberOfMatches(self, n: int) -> int:
        # Time: O(1), Space: O(1)

        # result = 0
        #
        # while n > 1:
        #     if n % 2 == 0:
        #         result += n / 2
        #         n = n / 2
        #     else:
        #         result += (n - 1) / 2
        #         n = 1 + (n - 1) / 2
        #
        # return int(result)

        return n - 1


if __name__ == "__main__":
    solution = Solution()

    assert solution.numberOfMatches(n=7) == 6

    assert solution.numberOfMatches(n=14) == 13
