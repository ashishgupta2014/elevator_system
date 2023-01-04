import heapq

from source.elevator_car.command import Command
from source.elevator_car.direction import Direction
from source.elevator_car.elevator_car import ElevatorCar


class ElevatorController:
    """Elevator Controller"""

    def __init__(self, elevator_id: int):
        self.elevator_car: ElevatorCar = ElevatorCar(elevator_id=elevator_id)
        self._up_dir_min_heap = []
        self._down_dir_max_heap = []
        self._queue = []

    def review_queue(self):
        queue = self._queue.copy()
        self._queue = []
        for cmd in queue:
            self.serve_request(cmd)

    def run(self):
        print(f'Elevator {self.elevator_car.get_id()} Started.')
        while self._up_dir_min_heap or self._down_dir_max_heap:
            if self._up_dir_min_heap and self.elevator_car.get_direction() == Direction.UP.name:
                floor = heapq.heappop(self._up_dir_min_heap)
                print(f'Elevator Moving Direction ({Direction.UP.name}) and currently at floor ({floor})')
                self.elevator_car.set_direction_floor(direction=Direction.UP.name,
                                                      floor=floor)
                if not self._up_dir_min_heap:
                    print(f'Elevator Changing Direction ({Direction.DOWN.name}) and currently at floor ({floor})')
                    self.elevator_car.set_direction_floor(direction=Direction.DOWN.name,
                                                          floor=floor)
                    self.review_queue()
            elif self._down_dir_max_heap and self.elevator_car.get_direction() == Direction.DOWN.name:
                floor = -heapq.heappop(self._down_dir_max_heap)
                print(f'Elevator Moving Direction ({Direction.DOWN.name}) and currently at floor ({floor})')
                self.elevator_car.set_direction_floor(direction=Direction.DOWN.name,
                                                      floor=floor)
                if not self._down_dir_max_heap:
                    print(f'Elevator Changing Direction ({Direction.UP.name}) and currently at floor ({floor})')
                    self.elevator_car.set_direction_floor(direction=Direction.UP.name,
                                                          floor=floor)
                    self.review_queue()
            else:
                if self._up_dir_min_heap and not self._down_dir_max_heap:
                    floor = self.elevator_car.get_current_floor()
                    self.elevator_car.set_direction_floor(direction=Direction.UP.name,
                                                          floor=floor)
                    print(f'No one waiting at Down direction')
                    print(f'Elevator Changing Direction ({Direction.UP.name}) and currently at floor ({floor})')
                elif not self._up_dir_min_heap and self._down_dir_max_heap:
                    floor = self.elevator_car.get_current_floor()
                    self.elevator_car.set_direction_floor(direction=Direction.DOWN.name,
                                                          floor=floor)
                    print(f'No one waiting at Up direction')
                    print(f'Elevator Changing Direction ({Direction.DOWN.name}) and currently at floor ({floor})')
                else:
                    direction = self.elevator_car.get_direction()
                    floor = self.elevator_car.get_current_floor()
                    print(f'Lift Stuck unexpectedly at floor {floor} on moving direction ({direction}).')
                    print(f'Panic for up direction {self._up_dir_min_heap}')
                    print(f'Panic for down direction {self._down_dir_max_heap}')
                    print(f'Queued {self._queue}')

        print(f'Elevator {self.elevator_car.get_id()} Stopped.')

    def serve_request(self, command: Command):
        if self.elevator_car.get_direction() == Direction.IDEAL.name:  # lift is ideal or same direction
            if command.direction == Direction.UP.name:
                self.up(command)
            elif command.direction == Direction.DOWN.name:
                self.down(command)
            self.elevator_car.set_direction_floor(direction=command.direction, floor=command.current_floor)
        elif command.direction == Direction.UP.name \
                and command.current_floor >= self.elevator_car.get_current_floor():  # life is going up
            self.up(command)
        elif command.direction == Direction.DOWN.name \
                and command.current_floor <= self.elevator_car.get_current_floor():  # life is going down
            self.down(command)
        else:
            self.queued(command)

    def queued(self, command: Command):
        self._queue.append(command)

    def up(self, command: Command):
        heapq.heappush(self._up_dir_min_heap, command.desire_floor)

    def down(self, command: Command):
        heapq.heappush(self._down_dir_max_heap, -command.desire_floor)
