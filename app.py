import argparse
from pathlib import Path

import tomllib

from vpx_gamepad import VisualPinballXGamepad


def main():
    project = tomllib.load(
        Path(__file__).parent.joinpath("pyproject.toml").resolve().open("rb")
    )
    parser = argparse.ArgumentParser(
        prog="vpx_gamepad.exe",
        description=f"{project["project"]["description"]} v{project["project"]["version"]}",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="print verbose output",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="store_true",
        default=False,
        help="print the version number and exit",
    )
    args = parser.parse_args()
    try:
        if args.version:
            print(
                f"{project["project"]["description"]} v{project["project"]["version"]}"
            )
        else:
            VisualPinballXGamepad(
                verbose=args.verbose, version=project["project"]["version"]
            ).run()

    except KeyboardInterrupt:
        print("It was interrupted by the user.")


if __name__ == "__main__":
    main()
