from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = last_position = len(nums) - 1
        while i >= 0:
            if i + nums[i] >= last_position:
                last_position = i

            i -= 1

        return last_position == 0


if __name__ == '__main__':
    solution = Solution()

    assert solution.canJump(nums=[2, 3, 1, 1, 4]) is True
