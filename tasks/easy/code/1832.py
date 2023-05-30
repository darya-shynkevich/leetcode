# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram,
# or false otherwise.

# Constraints:
#
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.
from string import ascii_lowercase


class Solution:

    def checkIfPangram(self, sentence: str) -> bool:

        # Time: O(n), Space: O(1)

        return len(ascii_lowercase) == len(set(sentence))

    # Other ideas:

    # 1. Find letters one by one: Time O(n), Space O(1)
    # def checkIfPangram(self, sentence: str) -> bool:
    #     # We iterate over 'sentence' for 26 times, one for each letter 'curr_char'.
    #     for i in range(26):
    #         curr_char = chr(ord('a') + i)
    #
    #         # If 'sentence' doesn't contain 'curr_char', it is not a pangram.
    #         if sentence.find(curr_char) == -1:
    #             return False
    #
    #     # If we manage to find all 26 letters, it is a pangram.
    #     return True

    # 2. Set: Time O(n), Space O(1)
    # def checkIfPangram(self, sentence: str) -> bool:
    #     # Add every letter of 'sentence' to hash set 'seen'.
    #     seen = set(sentence)
    #
    #     # If the size of 'seen' is 26, then 'sentence' is a pangram.
    #     return len(seen) == 26

    # 3. Use Array as Counter: Time O(n), Space O(1)
    # def checkIfPangram(self, sentence: str) -> bool:
    #     # Array 'seen' of size 26.
    #     seen = [False] * 26
    #
    #     # For every letter 'currChar', we find its ASCII code,
    #     # and update value at the mapped index as true.
    #     for curr_char in sentence:
    #         seen[ord(curr_char) - ord('a')] = True
    #
    #     # Once we finish iterating, check if 'seen' contains false.
    #     for status in seen:
    #         if not status:
    #             return False
    #     return True

    # 4. Bit Manipulation: Time O(n), Space O(1)
    # def checkIfPangram(self, sentence: str) -> bool:
    #     # Initialize seen = 0 since we start with no letter.
    #     seen = 0
    #
    #     # Iterate over 'sentence'.
    #     for curr_char in sentence:
    #         # Map each 'curr_char' to its index using its ASCII code.
    #         mapped_index = ord(curr_char) - ord('a')
    #
    #         # 'curr_bit' represents the bit for 'curr_char'.
    #         curr_bit = 1 << mapped_index
    #
    #         # Use 'OR' operation since we only add its bit for once.
    #         seen |= curr_bit
    #
    #     # Once we finish iterating, check if 'seen' contains 26 bits of 1.
    #     return seen == (1 << 26) - 1


if __name__ == "__main__":
    solution = Solution()

    assert solution.checkIfPangram(sentence="thequickbrownfoxjumpsoverthelazydog") is True

    assert solution.checkIfPangram(sentence="leetcode") is False
