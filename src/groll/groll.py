"""A helpful, dice rolling goblin for the command line!"""

import sys

import click

__version__ = "0.0.1"


def parse(*args):
    """parse dice list into integer values"""
    click.echo(f"(g)rolling: {args}")


@click.command()
@click.option(
    "--version",
    is_flag=True,
    is_eager=True,
    help="Display version infomation and exit.",
)
@click.argument("dice", nargs=-1)
def cli(dice, **kwargs):
    """A helpful, dice rolling goblin for the command line!"""
    if kwargs["version"]:
        click.echo(f"groll v{__version__} - {__doc__}")
        sys.exit()
    parse(dice)


if __name__ == "__main__":
    cli(sys.argv[1:])
