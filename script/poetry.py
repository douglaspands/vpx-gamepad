import os
from pathlib import Path

from PIL import Image


def build():
    os.system(
        " ".join(
            [
                "pyinstaller",
                "-F",
                "--python-option",
                '"PYTHONDONTWRITEBYTECODE=1"',
                "--optimize",
                "2",
                "--name",
                "vpx_gamepad.exe",
                "--icon",
                ".\\script\\vpx_cm.ico",
                "--console",
                ".\\app.py",
            ]
        )
    )


def maker_ico():
    image_file = Path("script") / "vpx_cm.jpeg"
    jpeg_image = Image.open(image_file.open("rb"))
    jpeg_image.save(image_file.with_suffix(".ico"), format="ICO")


def lint():
    os.system("ruff check .")


def format():
    os.system("ruff format .")


def start():
    os.system("python .\\app.py")
