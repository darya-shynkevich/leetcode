from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        result = 0
        for num_1 in arr1:

            is_suitable = True

            for num_2 in arr2:
                if abs(num_1 - num_2) <= d:
                    is_suitable = False
                    break

            if is_suitable:
                result += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2) == 2

    assert solution.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3) == 2

    assert solution.findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6) == 1

    assert solution.findTheDistanceValue(arr1=[-3,-3,4,-1,-10], arr2=[7,10], d=12) == 1
