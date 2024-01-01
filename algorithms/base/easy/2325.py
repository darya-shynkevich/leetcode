# You are given the strings key and message, which represent a cipher key and a secret message,
# respectively. The steps to decode message are as follows:
#
# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet),
# we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
# Return the decoded message.

# Constraints:
#
# 26 <= key.length <= 2000
# key consists of lowercase English letters and ' '.
# key contains every letter in the English alphabet ('a' to 'z') at least once.
# 1 <= message.length <= 2000
# message consists of lowercase English letters and ' '.

from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        translation_map = {' ': ' '}
        pointer = 0
        for i, letter in enumerate(key):
            if not translation_map.get(letter):
                translation_map.update({letter: ascii_lowercase[pointer]})
                pointer += 1

        trans_table = message.maketrans(translation_map)
        return message.translate(trans_table)


if __name__ == "__main__":
    solution = Solution()

    assert solution.decodeMessage(key="the quick brown fox jumps over the lazy dog", message="vkbs bs t suepuv") == (
        "this is a secret"
    )

    assert solution.decodeMessage(
        key="eljuxhpwnyrdgtqkviszcfmabo", message="zwx hnfx lqantp mnoeius ycgk vcnjrdb"
    ) == "the five boxing wizards jump quickly"
