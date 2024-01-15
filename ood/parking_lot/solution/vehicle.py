import abc

from parking_level import ParkingLevel
from parking_spot import ParkingSpotType, ParkingSpot


class Vehicle(abc.ABC):

    REQUIRED_SPOTS = 1

    def __init__(self, uuid: int):
        self.uuid = uuid

    @abc.abstractmethod
    def can_fit_in_spot(self, spot: ParkingSpot):
        pass

    @abc.abstractmethod
    def can_be_placed_on_level(self, level: ParkingLevel):
        pass


class Car(Vehicle):
    def can_fit_in_spot(self, spot: ParkingSpot):
        return spot.spot_type in (ParkingSpotType.LARGE, ParkingSpotType.COMPACT)

    def can_be_placed_on_level(self, level: ParkingLevel):
        for spot in level.parking_spots:
            if self.can_fit_in_spot(spot):
                return True
        return False


class Bus(Vehicle):

    REQUIRED_SPOTS = 5

    def can_fit_in_spot(self, spot: ParkingSpot):
        return spot.spot_type == ParkingSpotType.LARGE

    def can_be_placed_on_level(self, level: ParkingLevel):
        large_spot_count = 0
        for spot in level.parking_spots:
            if spot.spot_type == ParkingSpotType.LARGE:
                large_spot_count += 1

        return large_spot_count >= Bus.REQUIRED_SPOTS


class Motorbike(Vehicle):
    def can_fit_in_spot(self, spot: ParkingSpot):
        return True

    def can_be_placed_on_level(self, level: ParkingLevel):
        return level.parking_spots
