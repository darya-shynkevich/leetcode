# There is a special keyboard with all keys in a single row.
#
# Given a string keyboard of length 26 indicating the layout of the keyboard
# (indexed from 0 to 25). Initially, your finger is at index 0.
# To type a character, you have to move your finger to the index of the desired character.
# The time taken to move your finger from index i to index j is |i - j|.
#
# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.
#
# Constraints:
#
# keyboard.length == 26
# keyboard contains each English lowercase letter exactly once in some order.
# 1 <= word.length <= 104
# word[i] is an English lowercase letter.


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        if not word or not keyboard:
            return 0

        keyboard_map = {key: i for i, key in enumerate(keyboard)}

        result = pointer = 0
        for char in word:
            char_position = keyboard_map[char]
            result += abs(pointer - char_position)
            pointer = char_position

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.calculateTime(keyboard="abcdefghijklmnopqrstuvwxyz", word="cba") == 4

    assert solution.calculateTime(keyboard="pqrstuvwxyzabcdefghijklmno", word="leetcode") == 73
