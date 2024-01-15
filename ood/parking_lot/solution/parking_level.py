from typing import List

from parking_spot import ParkingSpot


class ParkingLevel:

    def __init__(self, level_id: int, parking_spots: List[ParkingSpot]):
        self.level_id = level_id
        self.parking_spots = parking_spots

    def assign_vehicle(self, vehicle):
        if vehicle.can_be_placed_on_level(self):
            required_spots = vehicle.REQUIRED_SPOTS
            for spot in self.parking_spots:
                if spot.assign_vehicle(vehicle=vehicle):
                    required_spots -= 1

                if required_spots == 0:
                    return True

        return False
