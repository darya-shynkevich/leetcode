# You are given an integer n and an integer start.
#
# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
#
# Return the bitwise XOR of all elements of nums.

# Constraints:
#
# 1 <= n <= 1000
# 0 <= start <= 1000
# n == nums.length


class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        # Time: O(n), Space: O(1)

        result = start
        for i in range(1, n):
            result = result ^ (start + 2 * i)

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.xorOperation(n=5, start=0) == 8

    assert solution.xorOperation(n=4, start=3) == 8
