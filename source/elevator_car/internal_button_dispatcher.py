from typing import List

from source.elevator_car.command import Command
from source.elevator_car.elevator_controller import ElevatorController


class InternalButtonDispatcher:
    """Internal Button Dispatcher"""
    _elevator_controllers: List[ElevatorController] = []

    def create_elevator_controller(self, lift: int):
        self._elevator_controllers.append(ElevatorController(elevator_id=lift))

    def submit_request(self, elevator_id, command: Command):
        elevator_controller: ElevatorController = self._elevator_controllers[elevator_id]
        elevator_controller.serve_request(command)

    def run(self):
        for elevator in self._elevator_controllers:
            elevator.run()
