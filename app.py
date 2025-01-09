import argparse

import tomllib

from vpx_gamepad import VisualPinballXGamepad


def main():
    with open(r".\pyproject.toml", "rb") as file:
        project = tomllib.load(file)

    parser = argparse.ArgumentParser(
        prog="vpx_gamepad.exe",
        description=f"{project["project"]["description"]} {project["project"]["version"]}",
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
                f"{VisualPinballXGamepad.__name__} {VisualPinballXGamepad.__version__}"
            )
        else:
            VisualPinballXGamepad(
                verbose=args.verbose, version=project["project"]["version"]
            ).run()

    except KeyboardInterrupt:
        print("It was interrupted by the user.")


if __name__ == "__main__":
    main()
