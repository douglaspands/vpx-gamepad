import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


from .vpx_gamepad import VisualPinballXGamepad

__all__ = ("VisualPinballXGamepad",)
