# Given an integer array sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

from typing import List


def solution(nums: List[int]) -> List[int]:
    n = len(nums)

    start, end = 0, n - 1

    result = [0] * n
    index = n - 1

    while end > -1 and index > -1:
        if abs(nums[start]) < abs(nums[end]):
            result[index] = nums[end] ** 2
            end -= 1
        else:
            result[index] = nums[start] ** 2
            start += 1

        index -= 1

    return result


if __name__ == "__main__":

    assert solution(nums=[-4, -3, 0, 1, 10]) == [0, 1, 9, 16, 100]
