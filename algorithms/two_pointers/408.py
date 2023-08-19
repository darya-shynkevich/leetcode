class Solution:

    def _get_number(self, abbr, start):
        number = ''

        k = 0
        while start < len(abbr) and abbr[start].isdigit():
            number += abbr[start]
            k += 1
            start += 1

        return int(number), k

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        # T: O(n), S: O(10

        word_len = len(word)
        abbr_len = len(abbr)

        if abbr_len > word_len:
            return False

        if word == abbr:
            return True

        i = j = 0
        while i < abbr_len:

            if abbr[i].isdigit():

                if abbr[i] == '0':
                    return False

                number, k = self._get_number(abbr, i)

                if j + number == word_len and i + k == abbr_len:
                    return True

                if j + number > word_len - 1 or i + k > abbr_len - 1 or word[j + number] != abbr[i + k]:
                    return False

                i += k
                j += number

            else:
                if j > word_len - 1 or i > abbr_len - 1 or word[j] != abbr[i]:
                    return False

            i += 1
            j += 1

        return j == word_len and i == abbr_len



if __name__ == "__main__":
    solution = Solution()

    assert solution.validWordAbbreviation(word = "int", abbr = "i2") is True

    assert solution.validWordAbbreviation(word = "internationalization", abbr = "i12iz4n") is True

    assert solution.validWordAbbreviation(word = "apple", abbr = "a2e") is False

    assert solution.validWordAbbreviation(word="a", abbr="a") is True

    assert solution.validWordAbbreviation(word="hi", abbr="1") is False

    assert solution.validWordAbbreviation(word="hi", abbr="02") is False

    assert solution.validWordAbbreviation(word="cccc", abbr="c2ca") is False
