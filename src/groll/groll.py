"""A helpful, dice rolling goblin for the command line!"""
from groll import __version__


def cli():
    """entrypoint for CLI"""
    print(f"groll v{__version__} - {__doc__}")


if __name__ == "__main__":
    cli()
