class TwoSum:

    def __init__(self):
        self.numbers = {}
        self.numbers_len = 0

    def add(self, number: int) -> None:
        counter = self.numbers.get(number, 0)
        self.numbers[number] = counter + 1

        self.numbers_len += 1

    def find(self, value: int) -> bool:
        if self.numbers_len in [0, 1]:
            return False

        for number in self.numbers:
            target_number = value - number
            if number == target_number and self.numbers.get(target_number) < 2:
                continue

            if value - number in self.numbers:
                return True

        return False


if __name__ == "__main__":
    # Your TwoSum object will be instantiated and called as such:
    obj = TwoSum()
    obj.add(1)
    obj.add(3)
    obj.add(5)

    assert obj.find(4) is True
    assert obj.find(7) is False

    obj = TwoSum()
    obj.add(0)
    obj.add(0)

    assert obj.find(0) is True

    obj = TwoSum()
    obj.add(1)
    obj.add(2)

    assert obj.find(1) is False

    obj = TwoSum()
    obj.add(3)
    obj.add(2)
    obj.add(1)

    assert obj.find(2) is False
