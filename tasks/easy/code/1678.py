# You own a Goal Parser that can interpret a string command.
# The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
# The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
# The interpreted strings are then concatenated in the original order.
#
# Given the string command, return the Goal Parser's interpretation of command.
#
# Constraints:
#
# 1 <= command.length <= 100
# command consists of "G", "()", and/or "(al)" in some order.


class Solution:
    def interpret(self, command: str) -> str:
        replacement_table = {"()": "o", "(al)": "al"}

        for original, replacement in replacement_table.items():
            command = command.replace(original, replacement)

        return command


if __name__ == "__main__":
    solution = Solution()

    assert solution.interpret(command="G()(al)") == "Goal"

    assert solution.interpret(command="G()()()()(al)") == "Gooooal"

    assert solution.interpret(command="(al)G(al)()()G") == "alGalooG"
