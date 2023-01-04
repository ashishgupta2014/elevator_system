from enum import Enum


class ButtonControl(Enum):
    INSIDE = 'Inside'
    OUTSIDE = 'Outside'

    @classmethod
    def get_button_name(cls, name):
        if cls.INSIDE.name.lower() == name.lower():
            return cls.INSIDE.name

        if cls.OUTSIDE.name.lower() == name.lower():
            return cls.OUTSIDE.name
        raise ValueError(f'Invalid Button Pressed {name}')
