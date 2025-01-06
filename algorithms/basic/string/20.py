class Solution:
    bracket_map = {"(": ")", "[": "]", "{": "}"}
    open_par = {"(", "[", "{"}

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in self.open_par:
                stack.append(char)
            elif stack and char == self.bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False

        return stack == []



if __name__ == '__main__':
    solution = Solution()

    assert solution.isValid(s="()")
    assert solution.isValid(s="()[]{}")
    assert solution.isValid(s="(]") is False
    assert solution.isValid(s="(])]") is False
    assert solution.isValid(s="([)]") is False
