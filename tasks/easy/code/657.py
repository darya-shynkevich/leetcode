# There is a robot starting at the position (0, 0), the origin, on a 2D plane.
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
#
# You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move.
# Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
#
# Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.
#
# Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once,
# 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement
# is the same for each move.

# Constraints:
#
# 1 <= moves.length <= 2 * 104
# moves only contains the characters 'U', 'D', 'L' and 'R'.


class Solution:
    def judgeCircle(self, moves: str) -> bool:

        # Time: O(n), Space: O(n)

        robot_movement_map = {
            'U': 0,
            'D': 0,
            'L': 0,
            'R': 0,
        }

        for move in moves:
            robot_movement_map[move] += 1

        if robot_movement_map['U'] == robot_movement_map['D'] and robot_movement_map['L'] == robot_movement_map['R']:
            return True
        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.judgeCircle(moves="UD") is True

    assert solution.judgeCircle(moves="LL") is False
