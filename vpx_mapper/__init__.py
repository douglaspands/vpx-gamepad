import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


from .vpx_mapper import VisualPinballXMapper

__all__ = ("VisualPinballXMapper",)
