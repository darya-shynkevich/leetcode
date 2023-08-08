class Solution:

    def get_next_number(self, number):
        new_number = 0

        while number:
            last_digit = number % 10
            new_number += last_digit ** 2
            number //= 10

        return new_number


    # def isHappy(self, n: int) -> bool:
    #     # Time: O(log(n) * k), where n is the input number and k is the number of digits in the input number
    #     # Space: O(log(n)
    #
    #     number = n
    #     numbers = set()
    #     while True:
    #         next_number = self.get_next_number(number)
    #
    #         if next_number == 1:
    #             return True
    #
    #         if next_number in numbers:
    #             return False
    #
    #         numbers.add(next_number)
    #         number = next_number

    def isHappy(self, n: int) -> bool:
        # Floyd's Cycle-Finding Algorithm
        # Time: O(log(n)), Space: O(1)

        slow = n
        fast = self.get_next_number(n)

        while fast != 1 and slow != fast:
            slow = self.get_next_number(slow)
            fast = self.get_next_number(self.get_next_number(fast))

        return fast == 1


if __name__ == "__main__":
    solution = Solution()

    assert solution.isHappy(19) is True
    assert solution.isHappy(2) is False
