# You are given a positive integer num consisting only of digits 6 and 9.
#
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

# Constraints:
#
# 1 <= num <= 10^4
# num consists of only 6 and 9 digits.
from math import log10


class Solution:
    # def maximum69Number(self, num: int) -> int:
    #
    #     # Time: O(N), Space: O(N)
    #
    #     num_len = int(log10(num)) + 1
    #
    #     result = 0
    #     is_changed_digit = False
    #     for i, digit in enumerate(str(num)):
    #         current_digit = int(digit)
    #         if is_changed_digit is False and current_digit == 6:
    #             current_digit = 9
    #             is_changed_digit = True
    #
    #         result += current_digit * 10**(num_len - i - 1)
    #
    #     return result

    # def maximum69Number(self, num: int) -> int:
    #
    #     # Time: O(N), Space: O(N)
    #
    #     num_string = str(num)
    #
    #     return int(num_string.replace('6', '9', 1))

    def maximum69Number(self, num: int) -> int:

        # Time: O(N), Space: O(1)

        num_copy = num

        i = 0
        last_6_index = False
        while num_copy:
            current_digit = num_copy % 10
            if current_digit == 6:
                last_6_index = i

            num_copy //= 10
            i += 1

        if last_6_index is False:
            return num

        return num + 3 * 10 ** last_6_index


if __name__ == "__main__":
    solution = Solution()

    assert solution.maximum69Number(num=9669) == 9969

    assert solution.maximum69Number(num=9996) == 9999

    assert solution.maximum69Number(num=9999) == 9999
