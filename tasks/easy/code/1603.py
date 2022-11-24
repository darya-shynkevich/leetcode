# Design a parking system for a parking lot. The parking lot has three kinds of parking spaces:
# big, medium, and small, with a fixed number of slots for each size.
#
# Implement the ParkingSystem class:
#
# ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class.
# The number of slots for each parking space are given as part of the constructor.
# bool addCar(int carType) Checks whether there is a parking space of carType for the car
# that wants to get into the parking lot. carType can be of three kinds: big, medium, or small,
# which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType.
# If there is no space available, return false, else park the car in that size space and return true.

# 0 <= big, medium, small <= 1000
# carType is 1, 2, or 3
# At most 1000 calls will be made to addCar


class ParkingSystem:

    BIG_CAR = 1
    MEDIUM_CAR = 2
    SMALL_CAR = 3

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == self.BIG_CAR and self.big > 0:
            self.big -= 1
            return True
        elif carType == self.MEDIUM_CAR and self.medium > 0:
            self.medium -= 1
            return True
        elif carType == self.SMALL_CAR and self.small > 0:
            self.small -= 1
            return True
        return False


if __name__ == "__main__":
    parkingSystem = ParkingSystem(1, 1, 0)
    assert parkingSystem.addCar(1) is True
    assert parkingSystem.addCar(2) is True
    assert parkingSystem.addCar(3) is False
    assert parkingSystem.addCar(1) is False
