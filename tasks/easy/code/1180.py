# Given a string s, return the number of substrings that have only one distinct letter.

# Constraints:
#
# 1 <= s.length <= 1000
# s[i] consists of only lowercase English letters.

class Solution:
    def countLetters(self, s: str) -> int:
        s_map = {}
        for element in s:
            count = s_map.get(element, 0)
            s_map.update({element: count + 1})

        result = 0
        for value in s_map.values():
            breakpoint()
            result += sum([i for i in range(value + 1)])


        print(result)
        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.countLetters(s="aaaba") == 8

    assert solution.countLetters(s="aaaaaaaaaa") == 55
