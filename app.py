import argparse

from vpx_gamepad import VisualPinballXGamepad


def main():
    parser = argparse.ArgumentParser(
        prog="vpx_gamepad.exe",
        description="Visual Pinball X - Gamepad Mapper (v0.7.0)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="print verbose output",
    )
    args = parser.parse_args()
    try:
        VisualPinballXGamepad(verbose=args.verbose).run()
    except KeyboardInterrupt:
        print("It was interrupted by the user.")


if __name__ == "__main__":
    main()
