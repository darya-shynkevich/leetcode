# Given a valid (IPv4) IP address, return a defanged version of that IP address.
#
# A defanged IP address replaces every period "." with "[.]".

# The given address is a valid IPv4 address.


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


if __name__ == "__main__":
    solution = Solution()

    address = "1.1.1.1"

    assert solution.defangIPaddr(address=address) == "1[.]1[.]1[.]1"

    address = "255.100.50.0"

    assert solution.defangIPaddr(address=address) == "255[.]100[.]50[.]0"
