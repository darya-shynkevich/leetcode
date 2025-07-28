class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        result = 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                result = max(result, right - left)
            else:
                seen.remove(s[left])
                left += 1

        return result


solution = Solution()
print(solution.lengthOfLongestSubstring(s="abcabcbb"))
print(solution.lengthOfLongestSubstring(s="bbbbb"))
print(solution.lengthOfLongestSubstring(s="au"))
