

class Command:
    """Elevator Commands"""
    def __init__(self, current_floor: int, desire_floor: int, direction: str, button: str):
        self.current_floor = current_floor
        self.desire_floor = desire_floor
        self.direction = direction
        self.button = button
