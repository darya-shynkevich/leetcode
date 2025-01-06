# Given a string s, find the length of the longest substring without repeating characters.

def solution(s: str):
    result = 0
    char_set = set(s[0])

    len_s = len(s)

    for i in range(1, len_s - 1):
        if s[i] not in char_set:
            char_set.add(s[i])
        else:
            char_set = set()

        result = max(result, len(char_set))

    return result


if __name__ == "__main__":

    assert solution(s='abcabcbb') == 3

