from enum import Enum, IntEnum


class XboxControllerButtonEnum(IntEnum):
    SELECT = 6
    START = 7
    LB = 4
    RB = 5
    A = 0
    B = 1
    X = 2
    Y = 3


class XboxControllerDigitalEnum(Enum):
    _ = (0, 0)
    UP = (0, 1)
    DOWN = (0, -1)
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP_LEFT = (-1, 1)
    UP_RIGHT = (1, 1)
    DONW_LEFT = (-1, -1)
    DOWN_RIGHT = (1, -1)


class XboxControllerTriggerEnum(IntEnum):
    LT = 4
    RT = 5
