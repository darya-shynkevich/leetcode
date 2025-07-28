from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_seen = set()

        for i, num in enumerate(nums):
            if num in num_seen:
                return True

            num_seen.add(num)

            if len(num_seen) > k:
                num_seen.remove(nums[i-k])

        return False


solution = Solution()
print(solution.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
print(solution.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
print(solution.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
