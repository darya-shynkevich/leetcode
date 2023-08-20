class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        # T: O(n), S: O(n)

        len_s = len(s)

        if len_s in [0, 1]:
            return s

        arr_s = list(s)

        l, r = 0, len_s - 1
        while l <= r:
            left_isalpha = arr_s[l].isalpha()
            right_isalpha = arr_s[r].isalpha()

            if left_isalpha and right_isalpha:
                arr_s[l], arr_s[r] = arr_s[r], arr_s[l]
                l += 1
                r -= 1
            elif left_isalpha and not right_isalpha:
                r -= 1
            elif right_isalpha and not left_isalpha:
                l += 1
            else:
                l += 1
                r -= 1

        return ''.join(arr_s)


if __name__ == "__main__":
    solution = Solution()

    assert solution.reverseOnlyLetters(s = "ab-cd") == "dc-ba"

    assert solution.reverseOnlyLetters(s = "a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"

    assert solution.reverseOnlyLetters(s = "Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"

    assert solution.reverseOnlyLetters(s = "") == ""

    assert solution.reverseOnlyLetters(s = "a") == "a"

    assert solution.reverseOnlyLetters(s = "ab") == "ba"

    assert solution.reverseOnlyLetters(s = "/-+=") == "/-+="
