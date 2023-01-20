# Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

# Constraints:
#
# 1 <= s.length <= 5000
# s consists of only lowercase English letters.


class Solution:
    # def canPermutePalindrome(self, s: str) -> bool:
    #
    #     # Time: O(N), Space: O(N)
    #
    #     counter = {}
    #     for char in s:
    #         count = counter.get(char, 0)
    #         counter.update({char: count + 1})
    #
    #     is_odd = False
    #     for char_count in counter.values():
    #         if char_count % 2 == 1:
    #             if is_odd is True:
    #                 return False
    #
    #             is_odd = True
    #
    #     return True

    def canPermutePalindrome(self, s: str) -> bool:

        # Time: O(N), Space: O(1)

        counter = set()
        for char in s:
            if char in counter:
                counter.remove(char)
            else:
                counter.add(char)

        return len(counter) <= 1


if __name__ == "__main__":
    solution = Solution()

    assert solution.canPermutePalindrome(s="code") is False

    assert solution.canPermutePalindrome(s="aab") is True

    assert solution.canPermutePalindrome(s="carerac") is True

    assert solution.canPermutePalindrome(s="aaa") is True

    assert solution.canPermutePalindrome(s="aaabbbaaa") is True
