"""A helpful, dice rolling goblin for the command line!"""

import sys

from groll import __version__


def cli(args=None):
    """entrypoint for CLI"""
    if not args:
        args = sys.argv[0 + 1 : :]
    if "-v" in args or "--version" in args:
        print(f"groll v{__version__} - {__doc__}")
    else:
        print(f"args supplied = {args}")


if __name__ == "__main__":
    cli()
