from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [str(nums[0])]

        i = 0
        result = []
        while i < len(nums):
            start = nums[i]
            while i < len(nums) - 1 and nums[i + 1] - nums[i] == 1:
                i += 1

            if start == nums[i]:
                result.append(str(nums[i]))
            else:
                result.append(f"{start}->{nums[i]}")

            i += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert solution.summaryRanges(nums=[0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]

    assert solution.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]

    assert solution.summaryRanges(nums=[1, 3]) == ["1", "3"]

    assert solution.summaryRanges(nums=[0, 1, 2]) == ["0->2"]
