import collections
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return [[]]

        result = []
        nums_map = collections.defaultdict(list)
        for i in range(len(nums)):
            nums_map[nums[i]].append(i)

        k_set = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target_number = - nums[i] - nums[j]
                if target_number in nums_map:
                    indexes = nums_map.get(target_number)
                    for k in indexes:
                        if k != i and k != j:
                            result.append([i, j, k])
                            k_set.add(k)

        print(result)
        return [list(_) for _ in result]



if __name__ == "__main__":
    solution = Solution()

    assert solution.threeSum(nums = [-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
