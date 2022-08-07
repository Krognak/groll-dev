"""A helpful, dice rolling goblin for the command line!"""

from __future__ import annotations

import random
import re
import sys
from collections import namedtuple
from typing import List, Union

import click

from . import __version__

Dice = namedtuple("Dice", ["num", "sides"])


def roll(match):
    """substitute dice rolls into match object, returning a string"""
    num, sides = match.group(0).split("d")
    num = int(num) if num else 1
    sides = int(sides)
    dice = Dice(num, sides)
    results = (str(random.randint(1, dice.sides)) for _ in range(dice.num))
    return "+".join(results)


def parse(args: str) -> List[Union[str, int]]:
    """Substitutes dice rolls and splits by operators."""
    dstring = re.sub(r"\d*d\d+", roll, args)
    return re.split(r"(\+|-|\*|\/)", dstring)


@click.command(no_args_is_help=True)
@click.option(
    "--version",
    is_flag=True,
    is_eager=True,
    help="Display version infomation and exit.",
)
@click.argument("args", nargs=-1)
def cli(args, **kwargs):
    """A helpful, dice rolling goblin for the command line!"""
    if kwargs["version"]:
        click.echo(f"groll v{__version__} - {__doc__}")
        sys.exit()
    else:
        parse("".join(args))


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
