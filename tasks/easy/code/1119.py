# Given a string s, remove the vowels "a", "e", "i", "o", and "u" from it, and return the new string.

# 1 <= s.length <= 1000
# s consists of only lowercase English letters.


class Solution:
    
    EXCLUDE_CHARACTERS = {"a", "e", "i", "o", "u"}
    
    def removeVowels(self, s: str) -> str:
        
        result = ""
        for char in s:
            if char in Solution.EXCLUDE_CHARACTERS:
                continue

            result += char

        return result


if __name__ == "__main__":
    solution = Solution()

    s = "leetcodeisacommunityforcoders"

    assert solution.removeVowels(s=s) == "ltcdscmmntyfrcdrs"

    s = "aeiou"

    assert solution.removeVowels(s=s) == ""
