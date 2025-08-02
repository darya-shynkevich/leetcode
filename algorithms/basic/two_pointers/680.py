class Solution:
    def check_palindrome(self, s: str):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        wrong_character = None

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if wrong_character is not None:
                    return False

                return self.check_palindrome(s[:left]+s[left+1:]) or self.check_palindrome(s[:right]+s[right+1:])

        return True


solution = Solution()
print(solution.validPalindrome("abc"))