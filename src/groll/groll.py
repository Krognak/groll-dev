"""A helpful, dice rolling goblin for the command line!"""

import random
import re
import sys

import click

from . import __version__

DICE_SYNTAX = r"\d*d\d+"
OPERATORS = r"\+|-|\*|\/"


def roll(dstring):
    """roll dice strings of the form [n]d[s]"""
    num, sides = dstring.group(0).split("d")
    if not num:
        num = 1
    else:
        num = int(num)
    sides = int(sides)
    return str(sum((random.randint(1, sides) for _ in range(num))))


def parse(dice):
    """parse dice list into integer values"""
    if not dice:
        dstring = "1d20"
    else:
        dstring = " ".join(dice)
    return re.sub(DICE_SYNTAX, roll, dstring)


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
    parsed_string = parse(dice)
    click.echo(parsed_string)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
