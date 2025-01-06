class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # T: O(max(n, m)), S: O(n + m)

        word1_len = len(word1)
        word2_len = len(word2)

        i = j = 0
        result = []
        while i < word1_len and j < word2_len:
            result.extend([word1[i], word2[j]])

            i += 1
            j += 1

        result.extend(word1[i:word1_len])
        result.extend(word2[j:word2_len])

        return ''.join(result)


if __name__ == "__main__":
    solution = Solution()

    assert solution.mergeAlternately(word1 = "abc", word2 = "pqr") == "apbqcr"

    assert solution.mergeAlternately(word1 = "ab", word2 = "pqrs") == "apbqrs"

    assert solution.mergeAlternately(word1 = "abcd", word2 = "pq") == "apbqcd"

    assert solution.mergeAlternately(word1="", word2="pqrs") == "pqrs"

    assert solution.mergeAlternately(word1="pqrs", word2="") == "pqrs"

    assert solution.mergeAlternately(word1="a", word2="b") == "ab"
