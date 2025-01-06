class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # T: O(len_t), S: O(1)

        len_s = len(s)
        len_t = len(t)

        if len_s == 0:
            return True

        if len_t == 0 or len_s > len_t:
            return False

        i = j = 0
        while i < len_t and j < len_s:
            if t[i] == s[j]:
                j += 1

            i += 1

        return j == len_s


if __name__ == "__main__":
    solution = Solution()

    assert solution.isSubsequence(s = "abc", t = "ahbgdc") is True

    assert solution.isSubsequence(s = "axc", t = "ahbgdc") is False

    assert solution.isSubsequence(s = "b", t = "abc") is True
