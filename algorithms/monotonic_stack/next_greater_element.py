"""

The Next greater Element for an element x is the first greater element on the right side of x in the array.
Elements for which no greater element exist, consider the next greater element as -1.

"""


def solution(input_arr: list[int]) -> list[int]:
    # T: O(N). S: O(N)

    n = len(input_arr)
    stack = []
    result = [-1] * n

    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= input_arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(input_arr[i])

    return result


if __name__ == "__main__":
    assert solution([4, 5, 2, 25]) == [5, 25, 25, -1]
    assert solution([13, 7, 6, 12]) == [-1, 12, 12, -1]
    assert solution([1, 2, 3]) == [2, 3, -1]
    assert solution([3, 2, 1]) == [-1, -1, -1]
