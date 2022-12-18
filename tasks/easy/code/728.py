# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
#
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

# Constraints:
#
# 1 <= left <= right <= 104
from typing import List


class Solution:

    def is_self_dividing(self, number: int):
        input_number = number
        while number:
            target_digit = number % 10
            if target_digit == 0:
                return False

            if input_number % target_digit:
                return False

            number = number // 10

        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for number in range(left, right + 1):
            if self.is_self_dividing(number):
                result.append(number)

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.selfDividingNumbers(left=1, right=22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

    assert solution.selfDividingNumbers(left=47, right=85) == [48, 55, 66, 77]
