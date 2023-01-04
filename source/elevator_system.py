from typing import List

from source.elevator_car.button import ButtonControl
from source.elevator_car.command import Command
from source.elevator_car.direction import Direction
from source.elevator_car.internal_button_dispatcher import InternalButtonDispatcher


class ElevatorSystem:
    """Elevator System Demo"""

    def __init__(self, no_of_lifts: int, floor_min: int, floor_max: int):
        self.no_of_lifts = no_of_lifts
        self.floor_min = floor_min
        self.floor_max = floor_max
        self.elevator_commands = dict()
        self.internal_button_dispatcher = InternalButtonDispatcher()
        for lift in range(self.no_of_lifts):
            self.internal_button_dispatcher.create_elevator_controller(lift=lift)

    def command_handler(self, requests):
        """Algo to validate which elevator going to run which command. currently it fixed to each elevator"""
        for index, elevator in enumerate(requests):

            commands = []
            for r in elevator:
                if len(r) != 4:
                    raise ValueError('Invalid Command format')
                button = ButtonControl.get_button_name(r[3])
                direction = Direction.get_direction_name(r[2])
                commands.append(Command(
                    current_floor=r[0],
                    desire_floor=r[1],
                    direction=direction,
                    button=button
                ))
            self.elevator_commands[index] = commands

    def start(self):
        for index, cmds in self.elevator_commands.items():
            for cmd in cmds:
                self.internal_button_dispatcher.submit_request(elevator_id=index, command=cmd)
        self.internal_button_dispatcher.run()

