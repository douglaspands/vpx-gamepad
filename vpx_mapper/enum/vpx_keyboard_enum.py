from enum import Enum

from pynput.keyboard import Key


class VpxKeyboardEnum(Enum):
    START = "1"
    COIN = "5"
    PLUNGER = Key.enter
    LEFT_FLIPPER = Key.shift_l
    RIGHT_FLIPPER = Key.shift_r
    LEFT_MAGNA = Key.ctrl_l
    RIGHT_MAGNA = Key.ctrl_r
    PAUSE = Key.esc
