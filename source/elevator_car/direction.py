from enum import Enum


class Direction(Enum):
    """Elevator Direction Constant"""
    UP = 'UP'
    DOWN = 'DOWN'
    IDEAL = 'IDEAL'

    @classmethod
    def get_direction_name(cls, name):
        if cls.UP.name.lower() == name.lower():
            return cls.UP.name

        if cls.DOWN.name.lower() == name.lower():
            return cls.DOWN.name

        if cls.IDEAL.name.lower() == name.lower():
            return cls.IDEAL.name

        raise ValueError(f'Invalid Direction {name}')
