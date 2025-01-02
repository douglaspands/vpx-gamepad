from __future__ import annotations

import logging

import pygame
from pynput.keyboard import Controller

from vpx_mapper.enum.gamepad_enum import GamepadEnum
from vpx_mapper.enum.vpx_keyboard_enum import VpxKeyboardEnum
from vpx_mapper.enum.xbox_enum import (
    XboxControllerButtonEnum,
    XboxControllerDigitalEnum,
    XboxControllerTriggerEnum,
)


class VisualPinballXMapper:
    def __init__(self, verbose=False):
        self.logger = logging.getLogger(VisualPinballXMapper.__name__)
        self.logger.setLevel(logging.DEBUG if verbose else logging.INFO)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s.%(msecs)03d - %(name)s - %(levelname)-8s - %(message)s",
                datefmt=r"%Y-%m-%d %H:%M:%S",
            )
        )
        self.logger.addHandler(console_handler)
        self.logger.info(f"{VisualPinballXMapper.__name__} init")

        self.keyboard = Controller()

        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

        if self.joystick.get_name() not in GamepadEnum:
            raise Exception(f"Controller not supported {self.joystick.get_name()}")

        self.logger.info(f"Using gamepad: {self.joystick.get_name()}")

        self.joystick_digital_last_press = XboxControllerDigitalEnum._.value
        self.keyboard_digital_last_press = None
        self.joystick_axis_last_press = None

    def run(self):
        while True:
            for event in pygame.event.get():
                self.logger.debug(f"{event=}")

                if event.type in (pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN):
                    kb_func = (
                        "press" if event.type == pygame.JOYBUTTONDOWN else "release"
                    )
                    match event.button:
                        case XboxControllerButtonEnum.A:
                            getattr(self.keyboard, kb_func)(
                                VpxKeyboardEnum.PLUNGER.value
                            )
                            self.logger.info(
                                f"{kb_func.capitalize():7} : {XboxControllerButtonEnum.A=} > {VpxKeyboardEnum.PLUNGER=}"
                            )
                        case XboxControllerButtonEnum.LB:
                            getattr(self.keyboard, kb_func)(
                                VpxKeyboardEnum.LEFT_FLIPPER.value
                            )
                            self.logger.info(
                                f"{kb_func.capitalize():7} : {XboxControllerButtonEnum.LB=} > {VpxKeyboardEnum.LEFT_FLIPPER=}"
                            )
                        case XboxControllerButtonEnum.RB:
                            getattr(self.keyboard, kb_func)(
                                VpxKeyboardEnum.RIGHT_FLIPPER.value
                            )
                            self.logger.info(
                                f"{kb_func.capitalize():7} : {XboxControllerButtonEnum.RB=} > {VpxKeyboardEnum.RIGHT_FLIPPER=}"
                            )
                        case XboxControllerButtonEnum.SELECT:
                            getattr(self.keyboard, kb_func)(VpxKeyboardEnum.PAUSE.value)
                            self.logger.info(
                                f"{kb_func.capitalize():7} : {XboxControllerButtonEnum.SELECT=} > {VpxKeyboardEnum.PAUSE=}"
                            )
                        case XboxControllerButtonEnum.START:
                            getattr(self.keyboard, kb_func)(VpxKeyboardEnum.START.value)
                            self.logger.info(
                                f"{kb_func.capitalize():7} : {XboxControllerButtonEnum.START=} > {VpxKeyboardEnum.START=}"
                            )
                        case _:
                            pass

                elif event.type == pygame.JOYHATMOTION:
                    kb_func = "press"
                    match event.value:
                        case XboxControllerDigitalEnum.LEFT.value:
                            getattr(self.keyboard, kb_func)(
                                VpxKeyboardEnum.LEFT_MAGNA.value
                            )
                            self.logger.info(
                                f"{kb_func.capitalize():7} : {XboxControllerDigitalEnum.LEFT=} > {VpxKeyboardEnum.LEFT_MAGNA=}"
                            )
                            self.joystick_digital_last_press = (
                                XboxControllerDigitalEnum.LEFT
                            )
                            self.keyboard_digital_last_press = (
                                VpxKeyboardEnum.LEFT_MAGNA
                            )
                        case XboxControllerDigitalEnum.RIGHT.value:
                            getattr(self.keyboard, kb_func)(
                                VpxKeyboardEnum.RIGHT_MAGNA.value
                            )
                            self.logger.info(
                                f"{kb_func.capitalize():7} : {XboxControllerDigitalEnum.RIGHT=} > {VpxKeyboardEnum.RIGHT_MAGNA=}"
                            )
                            self.joystick_digital_last_press = (
                                XboxControllerDigitalEnum.RIGHT
                            )
                            self.keyboard_digital_last_press = (
                                VpxKeyboardEnum.RIGHT_MAGNA
                            )

                        case _:
                            if self.keyboard_digital_last_press is not None:
                                kb_func = "release"
                                getattr(self.keyboard, kb_func)(
                                    self.keyboard_digital_last_press.value
                                )
                                self.logger.info(
                                    f"{kb_func.capitalize():7} : {self.joystick_digital_last_press=} > {self.keyboard_digital_last_press=}"
                                )
                                self.joystick_digital_last_press = (
                                    XboxControllerDigitalEnum._.value
                                )
                                self.keyboard_digital_last_press = None

                elif event.type == pygame.JOYAXISMOTION:
                    match event.axis:
                        case XboxControllerTriggerEnum.LT:
                            if event.value > 0.0:
                                kb_func = "press"
                                getattr(self.keyboard, kb_func)(
                                    VpxKeyboardEnum.COIN.value
                                )
                                self.logger.info(
                                    f"{kb_func.capitalize():7} : {XboxControllerTriggerEnum.LT=} ({event.value}) > {VpxKeyboardEnum.COIN=}"
                                )
                                self.joystick_axis_last_press = (
                                    VpxKeyboardEnum.COIN.value
                                )
                            elif self.joystick_axis_last_press is not None:
                                kb_func = "release"
                                getattr(self.keyboard, kb_func)(
                                    VpxKeyboardEnum.COIN.value
                                )
                                self.logger.info(
                                    f"{kb_func.capitalize():7} : {XboxControllerTriggerEnum.LT=} ({event.value}) > {VpxKeyboardEnum.COIN=}"
                                )
                                self.joystick_axis_last_press = None

                        case XboxControllerTriggerEnum.RT.value:
                            axis = self.joystick.get_axis(
                                XboxControllerTriggerEnum.RT.value
                            )
                            self.logger.debug(f"{axis=}")

                        case _:
                            pass

                else:
                    pass


__all__ = ("VisualPinballXMapper",)
