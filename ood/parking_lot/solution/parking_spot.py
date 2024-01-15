import abc
from enum import Enum


class ParkingSpotType(Enum):

    MOTORCYCLE = 0
    COMPACT = 1
    LARGE = 2


class ParkingSpot(abc.ABC):
    SPOT_TYPE = None

    def __init__(self, uuid: str, is_free: bool = True, vehicle = None):
        self.uuid = uuid
        self.is_free = is_free
        self.vehicle = vehicle

    @property
    def spot_type(self):
        return self.SPOT_TYPE

    def assign_vehicle(self, vehicle):
        if self.is_free and vehicle.can_fit_in_spot(self):
            self.is_free = False
            self.vehicle = vehicle
            return True

    def remove_vehicle(self):
        pass


class LargeParkingSpot(ParkingSpot):
    SPOT_TYPE = ParkingSpotType.LARGE

    def assign_vehicle(self, vehicle):
        return super().assign_vehicle(vehicle=vehicle)


class CompactParkingSpot(ParkingSpot):
    SPOT_TYPE = ParkingSpotType.COMPACT

    def assign_vehicle(self, vehicle):
        return super().assign_vehicle(vehicle=vehicle)


class MotorbikeParkingSpot(ParkingSpot):
    SPOT_TYPE = ParkingSpotType.MOTORCYCLE

    def assign_vehicle(self, vehicle):
        return super().assign_vehicle(vehicle=vehicle)