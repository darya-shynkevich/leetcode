class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


if __name__ == '__main__':
    solution = Solution()

    assert solution.reverseWords(s="the sky is blue") == "blue is sky the"

    assert solution.reverseWords(s="  hello world  ") == "world hello"

    assert solution.reverseWords(s="a good   example") == "example good a"

    assert solution.reverseWords(s=" asdasd df f") == "f df asdasd"
