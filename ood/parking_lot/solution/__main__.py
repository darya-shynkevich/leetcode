import uuid

from parking_level import ParkingLevel
from parking_lot import ParkingLot
from parking_spot import CompactParkingSpot, MotorbikeParkingSpot, LargeParkingSpot
from vehicle import Motorbike, Bus

if __name__ == "__main__":
    parking_levels = [
        ParkingLevel(
            level_id=1,
            parking_spots=[
                *[MotorbikeParkingSpot(uuid=uuid.uuid4()) for _ in range(4)],
                *[CompactParkingSpot(uuid=uuid.uuid4()) for _ in range(10)],
                *[LargeParkingSpot(uuid=uuid.uuid4()) for _ in range(2)],
            ]
        ),
        ParkingLevel(
            level_id=2,
            parking_spots=[
                *[CompactParkingSpot(uuid=uuid.uuid4()) for _ in range(5)],
                *[LargeParkingSpot(uuid=uuid.uuid4()) for _ in range(5)],
            ]
        ),
        ParkingLevel(
            level_id=3,
            parking_spots=[
                *[MotorbikeParkingSpot(uuid=uuid.uuid4()) for _ in range(2)],
                *[LargeParkingSpot(uuid=uuid.uuid4()) for _ in range(2)],
            ]
        ),
    ]
    parking_lot = ParkingLot(name='My parking lock', parking_levels=parking_levels)

    parking_lot.enter(vehicle=Motorbike(uuid=uuid.uuid4()))
    parking_lot.enter(vehicle=Bus(uuid=uuid.uuid4()))
    parking_lot.enter(vehicle=Bus(uuid=uuid.uuid4()))
