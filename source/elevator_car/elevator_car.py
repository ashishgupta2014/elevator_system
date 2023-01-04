from source.elevator_car.display import Display


class ElevatorCar:
    """Elevator Data model"""
    def __init__(self, elevator_id: int):
        self._id = elevator_id
        self._display = Display()

    def get_direction(self):
        return self._display.direction

    def get_current_floor(self):
        return self._display.floor

    def set_direction_floor(self, direction: str, floor: int):
        self._display.floor = floor
        self._display.direction = direction

    def get_id(self):
        return self._id

