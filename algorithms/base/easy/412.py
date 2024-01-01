# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# Constraints:
#
# 1 <= n <= 10^4
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        # Time: O(N), Space: O(1)

        result = []

        for i in range(1, n + 1):
            is_divisible_by_3 = i % 3 == 0
            is_divisible_by_5 = i % 5 == 0

            num_as_str = ""

            if is_divisible_by_3:
                num_as_str += "Fizz"

            if is_divisible_by_5:
                num_as_str += "Buzz"

            if not num_as_str:
                num_as_str = str(i)

            result.append(num_as_str)

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.fizzBuzz(n=3) == ["1", "2", "Fizz"]

    assert solution.fizzBuzz(n=5) == ["1", "2", "Fizz", "4", "Buzz"]

    assert solution.fizzBuzz(n=15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"
    ]
