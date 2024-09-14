"""

Given array of integer, find the next smaller of next greater element of every element in array.

"""


def solution(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1][0] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1][1]

        if i < len(arr) - 1:
            stack.append((arr[i], arr[i + 1]))

    return result


if __name__ == "__main__":
    assert solution([5, 1, 9, 2, 5, 1, 7]) == [2,  2, -1,  1, -1, -1, -1]
    assert solution([4, 8, 2, 1, 9, 5, 6, 3]) == [2,  5,  5,  5, -1,  3, -1, -1]