import collections
from typing import List


class Solution:
    def threeSum(self, nums: List[int]):

        nums_map = collections.defaultdict(list)
        for i in range(len(nums)):
            nums_map[nums[i]].append(i)

        result = set()
        for i, val1 in enumerate(nums):
            for j, val2 in enumerate(nums[i+1:]):
                target_number = - val1 - val2

                triplets = tuple(sorted([val1, val2, target_number]))
                if all([
                    target_number in nums_map,
                    triplets not in result,
                ]):
                    result.add(triplets)

        print(result)

        return result

if __name__ == "__main__":
    solution = Solution()

    assert sorted(solution.threeSum(nums = [-1,0,1,2,-1,-4])) == sorted({(-1, 0, 1), (-1, -1, 2)})
