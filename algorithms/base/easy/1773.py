# You are given an array items, where each items[i] = [typei, colori, namei] describes the type,
# color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.
#
# The ith item is said to match the rule if one of the following is true:
#
# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

# Constraints:
#
# 1 <= items.length <= 104
# 1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
# ruleKey is equal to either "type", "color", or "name".
# All strings consist only of lowercase letters.

from typing import List


class Solution:

    @staticmethod
    def get_rule_position(ruleKey: str):
        if ruleKey == "type":
            return 0
        elif ruleKey == "color":
            return 1
        return 2

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        # Time: O(n), Space: O(1)

        match_count = 0

        position = self.get_rule_position(ruleKey)

        for item in items:
            if item[position] == ruleValue:
                match_count += 1

        return match_count


if __name__ == "__main__":
    solution = Solution()

    assert solution.countMatches(
        items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
        ruleKey="color", ruleValue="silver"
    ) == 1

    assert solution.countMatches(
        items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
        ruleKey="type", ruleValue="phone"
    ) == 2
