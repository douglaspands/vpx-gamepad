from __future__ import annotations

import logging
from typing import Generator

import pygame
from pygame.event import Event
from pynput.keyboard import Controller

from vpx_gamepad.enum.gamepad_enum import GamepadEnum
from vpx_gamepad.enum.vpx_keyboard_enum import VpxKeyboardEnum
from vpx_gamepad.enum.xbox_enum import (
    XboxControllerAnalogicEnum,
    XboxControllerButtonEnum,
    XboxControllerDigitalEnum,
    XboxControllerEventEnum,
    XboxControllerTriggerEnum,
)


class VisualPinballXGamepad:
    __description__ = "Visual Pinball X - Gamepad Mapper"
    __version__ = "v0.10.0"

    GAMEPAD_DEVICE_NUMBER = 0
    GAMEPAD_PRESS_BUTTON = "press"
    GAMEPAD_RELEASE_BUTTON = "release"
    GAMEPAD_ANALOGIC_ENABLED = 0.59
    GAMEPAD_TRIGGER_ENABLED = -1.00

    def __init__(self, verbose: bool = False):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            logging.Formatter(
                fmt="%(asctime)s.%(msecs)03d - %(levelname)-8s - %(message)s",
                datefmt=r"%Y-%m-%d %H:%M:%S",
            )
        )
        self._logger = logging.getLogger("vpx_gamepad")
        self._logger.setLevel(logging.DEBUG if verbose else logging.INFO)
        self._logger.addHandler(console_handler)
        self._logger.info(
            f"Welcome to {VisualPinballXGamepad.__name__} {VisualPinballXGamepad.__version__}"
        )

        self._keyboard = Controller()

        pygame.init()
        pygame.joystick.init()

        try:
            self._joystick = pygame.joystick.Joystick(
                VisualPinballXGamepad.GAMEPAD_DEVICE_NUMBER
            )
        except BaseException:
            raise Exception("Gamepad device not found")

        self._joystick.init()

        match gamepad_name := self._joystick.get_name():
            case GamepadEnum.XBOX_360:
                self._gamepad_event_enum = XboxControllerEventEnum
                self._gamepad_digital_enum = XboxControllerDigitalEnum
                self._gamepad_button_enum = XboxControllerButtonEnum
                self._gamepad_analogic_enum = XboxControllerAnalogicEnum
                self._gamepad_trigger_enum = XboxControllerTriggerEnum

            case _:
                raise Exception(f"Gamepad not supported {gamepad_name}")

        self._logger.info(f"Using gamepad: {gamepad_name}")

        self._joystick_digital_last_press = self._gamepad_digital_enum._.value
        self._keyboard_digital_last_press = None
        self._joystick_trigger_r_last_press = None
        self._joystick_analogic_left_last_press = None

    def run(self):
        for event in self._get_events():
            self._event_process(event)

    def _get_events(self) -> Generator[Event, None, None]:
        while True:
            for event in pygame.event.get():
                self._logger.debug(f"{event=}")
                yield event

    def _event_process(self, event: Event):
        if event.type in self._gamepad_event_enum.BUTTON.value:
            kb_func = (
                VisualPinballXGamepad.GAMEPAD_PRESS_BUTTON
                if event.type == pygame.JOYBUTTONDOWN
                else VisualPinballXGamepad.GAMEPAD_RELEASE_BUTTON
            )
            match event.button:
                case self._gamepad_button_enum.A:
                    getattr(self._keyboard, kb_func)(VpxKeyboardEnum.START.value)
                    self._logger.info(
                        f"{kb_func.capitalize():14} : {self._gamepad_button_enum.A!r} => {VpxKeyboardEnum.START!r}"
                    )
                case self._gamepad_button_enum.B:
                    getattr(self._keyboard, kb_func)(VpxKeyboardEnum.PLUNGER.value)
                    self._logger.info(
                        f"{kb_func.capitalize():14} : {self._gamepad_button_enum.B!r} => {VpxKeyboardEnum.PLUNGER!r}"
                    )
                case self._gamepad_button_enum.X:
                    getattr(self._keyboard, kb_func)(VpxKeyboardEnum.COIN.value)
                    self._logger.info(
                        f"{kb_func.capitalize():14} : {self._gamepad_button_enum.X!r} => {VpxKeyboardEnum.COIN!r}"
                    )
                case self._gamepad_button_enum.LB:
                    getattr(self._keyboard, kb_func)(VpxKeyboardEnum.LEFT_FLIPPER.value)
                    self._logger.info(
                        f"{kb_func.capitalize():14} : {self._gamepad_button_enum.LB!r} => {VpxKeyboardEnum.LEFT_FLIPPER!r}"
                    )
                case self._gamepad_button_enum.RB:
                    getattr(self._keyboard, kb_func)(
                        VpxKeyboardEnum.RIGHT_FLIPPER.value
                    )
                    self._logger.info(
                        f"{kb_func.capitalize():14} : {self._gamepad_button_enum.RB!r} => {VpxKeyboardEnum.RIGHT_FLIPPER!r}"
                    )
                case self._gamepad_button_enum.SELECT:
                    getattr(self._keyboard, kb_func)(VpxKeyboardEnum.PAUSE.value)
                    self._logger.info(
                        f"{kb_func.capitalize():14} : {self._gamepad_button_enum.SELECT!r} => {VpxKeyboardEnum.PAUSE!r}"
                    )
                case self._gamepad_button_enum.START:
                    getattr(self._keyboard, kb_func)(VpxKeyboardEnum.START.value)
                    self._logger.info(
                        f"{kb_func.capitalize():14} : {self._gamepad_button_enum.START!r} => {VpxKeyboardEnum.START!r}"
                    )
                case _:
                    pass

        elif event.type in self._gamepad_event_enum.DIGITAL.value:
            kb_func = VisualPinballXGamepad.GAMEPAD_PRESS_BUTTON
            match event.value:
                case self._gamepad_digital_enum.LEFT.value:
                    getattr(self._keyboard, kb_func)(VpxKeyboardEnum.LEFT_MAGNA.value)
                    self._logger.info(
                        f"{kb_func.capitalize():14} : {self._gamepad_digital_enum.LEFT!r} => {VpxKeyboardEnum.LEFT_MAGNA!r}"
                    )
                    self._joystick_digital_last_press = self._gamepad_digital_enum.LEFT
                    self._keyboard_digital_last_press = VpxKeyboardEnum.LEFT_MAGNA
                case self._gamepad_digital_enum.RIGHT.value:
                    getattr(self._keyboard, kb_func)(VpxKeyboardEnum.RIGHT_MAGNA.value)
                    self._logger.info(
                        f"{kb_func.capitalize():14} : {self._gamepad_digital_enum.RIGHT!r} => {VpxKeyboardEnum.RIGHT_MAGNA!r}"
                    )
                    self._joystick_digital_last_press = self._gamepad_digital_enum.RIGHT
                    self._keyboard_digital_last_press = VpxKeyboardEnum.RIGHT_MAGNA

                case _:
                    if self._keyboard_digital_last_press is not None:
                        kb_func = VisualPinballXGamepad.GAMEPAD_RELEASE_BUTTON
                        getattr(self._keyboard, kb_func)(
                            self._keyboard_digital_last_press.value
                        )
                        self._logger.info(
                            f"{kb_func.capitalize():14} : {self._joystick_digital_last_press!r} => {self._keyboard_digital_last_press!r}"
                        )
                        self._joystick_digital_last_press = (
                            self._gamepad_digital_enum._.value
                        )
                        self._keyboard_digital_last_press = None

        elif event.type in self._gamepad_event_enum.ANALOGIC_OR_TRIGGER.value:
            match event.axis:
                case self._gamepad_trigger_enum.LT.value:
                    pass

                case self._gamepad_trigger_enum.RT.value:
                    if event.value > VisualPinballXGamepad.GAMEPAD_TRIGGER_ENABLED:
                        if self._joystick_trigger_r_last_press is None:
                            kb_func = VisualPinballXGamepad.GAMEPAD_PRESS_BUTTON
                            getattr(self._keyboard, kb_func)(
                                VpxKeyboardEnum.PLUNGER.value
                            )
                            self._logger.info(
                                f"{kb_func.capitalize():14} : {self._gamepad_trigger_enum.RT!r} ({event.value}) => {VpxKeyboardEnum.PLUNGER!r}"
                            )
                            self._joystick_trigger_r_last_press = (
                                VpxKeyboardEnum.PLUNGER.value
                            )
                    elif self._joystick_trigger_r_last_press is not None:
                        kb_func = VisualPinballXGamepad.GAMEPAD_RELEASE_BUTTON
                        getattr(self._keyboard, kb_func)(VpxKeyboardEnum.PLUNGER.value)
                        self._logger.info(
                            f"{kb_func.capitalize():14} : {self._gamepad_trigger_enum.RT!r} ({event.value}) => {VpxKeyboardEnum.PLUNGER!r}"
                        )
                        self._joystick_trigger_r_last_press = None

                case _:
                    if self._joystick_analogic_left_last_press is not None:
                        kb_func = VisualPinballXGamepad.GAMEPAD_RELEASE_BUTTON
                        self._logger.info(
                            f"{kb_func.capitalize() + " [fake]":14} : {self._joystick_analogic_left_last_press[0]!r} ({event.value}) => {self._joystick_analogic_left_last_press[1]!r}"
                        )
                        self._joystick_analogic_left_last_press = None

                    if event.axis == self._gamepad_analogic_enum.LEFT_X:
                        if event.value <= (
                            VisualPinballXGamepad.GAMEPAD_ANALOGIC_ENABLED * -1
                        ):
                            kb_func = VisualPinballXGamepad.GAMEPAD_PRESS_BUTTON
                            self._logger.info(
                                f"{kb_func.capitalize() + " [fake]":14} : {self._gamepad_analogic_enum.LEFT_X!r} ({event.value}) => {VpxKeyboardEnum.NUDGE_LEFT!r}"
                            )
                            self._joystick_analogic_left_last_press = (
                                self._gamepad_analogic_enum.LEFT_X,
                                VpxKeyboardEnum.NUDGE_LEFT,
                            )

                        elif (
                            event.value
                            >= VisualPinballXGamepad.GAMEPAD_ANALOGIC_ENABLED
                        ):
                            kb_func = VisualPinballXGamepad.GAMEPAD_PRESS_BUTTON
                            self._logger.info(
                                f"{kb_func.capitalize() + " [fake]":14} : {self._gamepad_analogic_enum.LEFT_X!r} ({event.value}) => {VpxKeyboardEnum.NUDGE_RIGHT!r}"
                            )
                            self._joystick_analogic_left_last_press = (
                                self._gamepad_analogic_enum.LEFT_X,
                                VpxKeyboardEnum.NUDGE_RIGHT,
                            )

                    elif event.axis == self._gamepad_analogic_enum.LEFT_Y:
                        if event.value <= (
                            VisualPinballXGamepad.GAMEPAD_ANALOGIC_ENABLED * -1
                        ):
                            kb_func = VisualPinballXGamepad.GAMEPAD_PRESS_BUTTON
                            self._logger.info(
                                f"{kb_func.capitalize() + " [fake]":14} : {self._gamepad_analogic_enum.LEFT_Y!r} ({event.value}) => {VpxKeyboardEnum.NUDGE_FWD!r}"
                            )
                            self._joystick_analogic_left_last_press = (
                                self._gamepad_analogic_enum.LEFT_Y,
                                VpxKeyboardEnum.NUDGE_FWD,
                            )

                        elif (
                            event.value
                            >= VisualPinballXGamepad.GAMEPAD_ANALOGIC_ENABLED
                        ):
                            kb_func = VisualPinballXGamepad.GAMEPAD_PRESS_BUTTON
                            self._logger.info(
                                f"{kb_func.capitalize() + " [fake]":14} : {self._gamepad_analogic_enum.LEFT_Y!r} ({event.value}) => {VpxKeyboardEnum.TILT_MECH!r}"
                            )
                            self._joystick_analogic_left_last_press = (
                                self._gamepad_analogic_enum.LEFT_Y,
                                VpxKeyboardEnum.TILT_MECH,
                            )


__all__ = ("VisualPinballXGamepad",)
