# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
# as follows:
#
# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
#
# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-",
# and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.

# 1 <= words.length <= 100
# 1 <= words[i].length <= 12
# words[i] consists of lowercase English letters.

from typing import List
from string import ascii_uppercase


class Solution:

    LETTER_TO_MORSE_CODE = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..'
    }

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapping_tbl = ascii_uppercase.maketrans(self.LETTER_TO_MORSE_CODE)

        transformations = set()
        for word in words:
            transformations.add(word.translate(mapping_tbl))

        return len(transformations)


if __name__ == "__main__":
    solution = Solution()

    assert solution.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"]) == 2

    assert solution.uniqueMorseRepresentations(words=["a"]) == 1
