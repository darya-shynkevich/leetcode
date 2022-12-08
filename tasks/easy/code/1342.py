# Given an integer num, return the number of steps to reduce it to zero.
#
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
#
# Constraints:
#
# 0 <= num <= 106


class Solution:
    def numberOfSteps(self, num: int) -> int:

        # Time O(log(n)), Space O(1)

        step = 0

        while num:
            num = num / 2 if num % 2 == 0 else num - 1
            step += 1

        return step


if __name__ == "__main__":
    solution = Solution()

    assert solution.numberOfSteps(num=14) == 6

    assert solution.numberOfSteps(num=8) == 4
