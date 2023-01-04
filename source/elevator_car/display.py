from source.elevator_car.direction import Direction


class Display:
    """Elevator Current Location Display"""
    def __init__(self):
        self.floor: 'int' = None
        self.direction: str = Direction.IDEAL.name

