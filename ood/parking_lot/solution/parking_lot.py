from typing import List

from loguru import logger

from parking_level import ParkingLevel
from vehicle import Vehicle


class ParkingLotMetaclass(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)

        return cls.instance


class ParkingLot(metaclass=ParkingLotMetaclass):

    def __init__(self, name: str, parking_levels: List[ParkingLevel]):
        self.name = name

        self.parking_levels = parking_levels

    def enter(self, vehicle: Vehicle):

        for level in self.parking_levels:
            if level.assign_vehicle(vehicle=vehicle):
                logger.info(f'Placed {vehicle.uuid} on level {level.level_id}')
                return

        logger.error(f'Can not place {vehicle.uuid} to parking lot {self.name}')

