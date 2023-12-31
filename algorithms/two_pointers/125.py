# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
import string


# Constraints:
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Time: O(n), Space: O(1)

        len_s = len(s)

        if len_s in [0, 1]:
            return True

        i, j = 0, len_s - 1
        while i < j:
            start = s[i].lower()
            end = s[j].lower()

            if start == end:
                i += 1
                j -= 1

            elif not start.isalnum():
                i += 1

            elif not end.isalnum():
                j -= 1

            else:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    assert solution.isPalindrome(s="A man, a plan, a canal: Panama") is True

    assert solution.isPalindrome(s="race a car") is False

    assert solution.isPalindrome(s=" ") is True
