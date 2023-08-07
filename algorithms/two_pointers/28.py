class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Time complexity: O(mn), Space complexity: O(n)

        if haystack == needle:
            return 0

        template_len = len(needle)

        for i in range(len(haystack) - template_len + 1):
            if haystack[i:i+template_len] == needle:
                return i

        return -1


if __name__ == "__main__":
    solution = Solution()

    assert solution.strStr(haystack = "sadbutsad", needle = "sad") == 0

    assert solution.strStr(haystack = "leetcode", needle = "leeto") == -1

    assert solution.strStr(haystack="abc", needle="c") == 2
