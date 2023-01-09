# There are n rings and each ring is either red, green, or blue. The rings are distributed across
# ten rods labeled from 0 to 9.
#
# You are given a string rings of length 2n that describes the n rings that are placed onto the rods.
# Every two characters in rings forms a color-position pair that is used to describe each ring where:
#
# The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
# The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
# For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3,
# a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.
#
# Return the number of rods that have all three colors of rings on them.

# Constraints:
#
# rings.length == 2 * n
# 1 <= n <= 100
# rings[i] where i is even is either 'R', 'G', or 'B' (0-indexed).
# rings[i] where i is odd is a digit from '0' to '9' (0-indexed).


class Solution:
    def countPoints(self, rings: str) -> int:

        # Time: O(n), Space: O(n)

        rings_map = {}
        for i in range(0, len(rings), 2):
            ring_number_to_colors = rings_map.get(rings[i+1])
            if ring_number_to_colors is not None:
                color = ring_number_to_colors.get(rings[i])
                if color is None:
                    ring_number_to_colors.update({rings[i]: True})
            else:
                rings_map.update({rings[i+1]: {rings[i]: True}})

        result = 0
        for color in rings_map.values():
            color_values = color.values()
            if len(color_values) == 3:
                result += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.countPoints(rings="B0B6G0R6R0R6G9") == 1

    assert solution.countPoints(rings="B0R0G0R9R0B0G0") == 1

    assert solution.countPoints(rings="G4") == 0
