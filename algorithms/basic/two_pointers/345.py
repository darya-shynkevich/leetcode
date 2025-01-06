class Solution:

    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def reverseVowels(self, s: str) -> str:
        # Time: O(n), Space: O(n)

        s = [char for char in s]

        i, j = 0, len(s) - 1
        while i < j:

            if s[j] not in self.vowels:
                j -= 1
                continue

            if s[j] in self.vowels and s[i] not in self.vowels:
                i += 1
                continue

            if s[i] in self.vowels and s[j] in self.vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return ''.join(s)


if __name__ == "__main__":
    solution = Solution()

    assert solution.reverseVowels(s = "hello") == "holle"

    assert solution.reverseVowels(s = "leetcode") == "leotcede"

    assert solution.reverseVowels(s="a.") == "a."

    assert solution.reverseVowels(s="aA") == "Aa"
