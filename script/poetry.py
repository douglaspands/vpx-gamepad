import os
from pathlib import Path


def shell_run(cmd: str):
    print(f"$ {cmd}")
    os.system(cmd)


def build():
    shell_run(
        " ".join(
            [
                "pyinstaller",
                "-F",
                "--python-option",
                '"PYTHONDONTWRITEBYTECODE=1"',
                "--name",
                "vpx_gamepad.exe",
                "--icon",
                r".\script\vpx_cm.ico",
                "--runtime-hook",
                r".\script\hook.py",
                "--add-data",
                r".\pyproject.toml:.\pyproject.toml",
                "--console",
                r".\app.py",
            ]
        )
    )


def maker_ico():
    from PIL import Image

    image_file = Path(input("Enter the file path: "))
    jpeg_image = Image.open(image_file.open("rb"))
    jpeg_image.save(image_file.with_suffix(".ico"), format="ICO")


def lint():
    shell_run("ruff check .")


def format():
    shell_run("ruff check --select I --fix .")
    shell_run("ruff format .")


def start():
    shell_run("python .\\app.py")
