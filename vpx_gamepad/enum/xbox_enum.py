from enum import Enum, IntEnum

import pygame


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


class XboxControllerAnalogicEnum(IntEnum):
    LEFT_X = 0
    LEFT_Y = 1
    RIGHT_X = 2
    RIGHT_Y = 3


class XboxControllerEventEnum(Enum):
    DIGITAL = (pygame.JOYHATMOTION,)
    BUTTON = (pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP)
    ANALOGIC_OR_TRIGGER = (pygame.JOYAXISMOTION,)
