from math import inf
from typing import List


class Solution:

    # Time:  O(n * m), where n is the number of strings in the input list and m is the length of the shortest string
    # Space: O(1)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_len = inf
        for _str in strs:
            shortest_len = min(shortest_len, len(_str))

        if shortest_len == 0:
            return ""

        result = None
        for i in range(shortest_len):
            current_char = strs[0][i]
            for j in range(1, len(strs)):
                result = i + 1
                if strs[j][i] != current_char:
                    if result is None:
                        return ""

                    return strs[0][:result - 1]

        return strs[0][:result]


if __name__ == '__main__':
    solution = Solution()

    assert solution.longestCommonPrefix(strs=["flower", "flow", "flight"]) == "fl"

    assert solution.longestCommonPrefix(strs=["dog", "racecar", "car"]) == ""

    assert solution.longestCommonPrefix(strs=["cardog", "carracecar", "car"]) == "car"

    assert solution.longestCommonPrefix(strs=["cir", "car"]) == "c"
