# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have.
# Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.


class Solution:

    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        sorted_stones = sorted(stones)

        sorted_jewels = sorted(jewels)
        last_jewel = sorted_jewels[len(sorted_jewels) - 1]

        jewels_map = {jewel: 1 for jewel in sorted_jewels}

        result = 0
        for stone in sorted_stones:
            if stone > last_jewel:
                continue

            if stone in jewels_map:
                result += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    jewels = "aA"
    stones = "aAAbbbb"

    assert solution.numJewelsInStones(jewels=jewels, stones=stones) == 3

    jewels = "z"
    stones = "ZZ"

    assert solution.numJewelsInStones(jewels=jewels, stones=stones) == 0

