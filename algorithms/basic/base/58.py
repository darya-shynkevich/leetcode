class Solution:

    # Time: O(N), Space: O(1)

    def lengthOfLastWord(self, s: str) -> int:
        len_s = len(s)

        result = 0
        for i in range(len_s - 1, -1, -1):
            if s[i] == " ":
                if result:
                    return result
                continue
            else:
                result += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    assert solution.lengthOfLastWord(s="Hello World") == 5

    assert solution.lengthOfLastWord(s="   fly me   to   the moon  ") == 4

    assert solution.lengthOfLastWord(s="luffy is still joyboy") == 6

    assert solution.lengthOfLastWord(s="") == 0

    assert solution.lengthOfLastWord(s="    ") == 0
