import argparse

import tomllib

from vpx_mapper import VisualPinballXMapper

with open("pyproject.toml", "rb") as f:
    pyproj = tomllib.load(f)


def main():
    parser = argparse.ArgumentParser(
        prog="vpx_mapper.exe",
        description=f"{pyproj["tool"]["poetry"]["description"]} (v{pyproj["tool"]["poetry"]["version"]})",
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
