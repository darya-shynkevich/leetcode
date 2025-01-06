"""

Given an array, print the Next Smaller Element (NSE) for every element.
The NSE for an element x is the first smaller element on the right side of x in the array.
Elements for which no smaller element exist (on the right side), consider NSE as -1.

"""


def solution(input_arr: list[int]) -> list[int]:
    # T: O(N). S: O(N)

    n = len(input_arr)
    stack = []
    result = [-1] * n

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] >= input_arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(input_arr[i])

    return result


if __name__ == "__main__":
    assert solution([4, 8, 5, 2, 25]) == [2, 5, 2, -1, -1]
    assert solution([13, 7, 6, 12]) ==  [7, 6, -1, -1]
    assert solution([1, 2, 3]) == [-1, -1, -1]
    assert solution([3, 2, 1]) == [2, 1, -1]