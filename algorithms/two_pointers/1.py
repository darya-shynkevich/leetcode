# Given an sorted array of integers, return the
# indices of the two numbers in it that add up to a specific "goal" number.

# Constraints
# Length of the array <= 100000
# The values of the array will be between -1000000000 and 1000000000
# The array can be empty
# The target sum will be between -1000000000 and 1000000000
# Expected time complexity : O(n * log(n))
# Expected space complexity : O(n)


def two_sum(nums, goal):
    len_nums = len(nums)

    start = 0
    end = len_nums - 1

    while start < end:
        if nums[start] + nums[end] < goal:
            start += 1
        elif nums[start] + nums[end] > goal:
            end -= 1
        else:
            return [start, end]

    return []


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert two_sum([1, 9, 13, 20, 47], 10) == [0, 1]
        print("PASSED: assert two_sum([1, 9, 13, 20, 47], 10) == [0, 1]")

    def test_2(self):
        assert two_sum([1, 2, 3, 4, 9], 12) == [2, 4]
        print("PASSED: assert two_sum([1, 2, 3, 4, 9], 12) == [2, 4]")

    def test_3(self):
        assert two_sum([], 10) == []
        print("PASSED: assert two_sum([], 10) == []")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
