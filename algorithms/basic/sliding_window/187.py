from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        k = 10

        seen = set()
        result = set()

        for i in range(len(s)):
            substr = s[i:i+k]
            if substr not in seen:
                seen.add(substr)
            else:
                result.add(substr)

        return list(result)


solution = Solution()
print(solution.findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
