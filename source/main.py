# https://github.com/ngautam0/elevator-system/blob/master/code/run.py
# https://tedweishiwang.github.io/journal/object-oriented-design-elevator.html
from source.elevator_system import ElevatorSystem


def main():
    # floors on which the button has been pressed in this sequence
    no_of_lifts, floor_min, floor_max = 2, -4, 20

    # default position of lifts, as of now we have got 5 lifts in place
    lift_positions = [9]

    elevator_sys = ElevatorSystem(no_of_lifts=no_of_lifts, floor_min=floor_min, floor_max=floor_max)
    # We can have multiple elevators. Array index is elevator id
    request_each = [[  # lift 0
        [9, 16, 'UP', 'Inside'],  # start location, desire location, direction, button pressed
        [3, 5, 'UP', 'Inside'],
        [1, 7, 'UP', 'Inside'],
        [16, 4, 'DOWN', 'outside'],
        [16, -2, 'DOWN', 'outside'],
        [1, 7, 'UP', 'outside'],
    ],
        [  # lift 1
            [16, 0, 'DOWN', 'outside'],  # start location, desire location, direction, button pressed
            [4, 5, 'UP', 'Inside'],
            [-2, 7, 'UP', 'Inside'],
            [8, -4, 'DOWN', 'outside'],
            [-2, 9, 'UP', 'outside'],
            [10, 0, 'DOWN', 'outside'],
        ]
    ]

    elevator_sys.command_handler(request_each)
    elevator_sys.start()


if __name__ == "__main__":
    main()
