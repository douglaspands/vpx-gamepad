import argparse

from vpx_mapper import VisualPinballXMapper


def main():
    parser = argparse.ArgumentParser(
        prog="vpx_mapper.exe",
        description="Visual Pinball X - Controller Mapper (v0.6.0)",
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
        vpx_mapper = VisualPinballXMapper(verbose=args.verbose)
        vpx_mapper.run()
    except KeyboardInterrupt:
        print("It was interrupted by the user.")


if __name__ == "__main__":
    main()
