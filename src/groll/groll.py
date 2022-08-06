"""A helpful, dice rolling goblin for the command line!"""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass
from typing import Generator, List, Tuple, Union

import click

from . import __version__


@dataclass()
class Dice:
    """Dice dataclass, defaults to a single die"""

    sides: int
    number: int = 1


def get_dice(dice_string: str) -> Dice:
    """Create Dice from string"""
    number, sides = dice_string.split("d")
    if number:
        dice = Dice(int(sides), int(number))
    else:
        dice = Dice(int(sides))
    return dice


def roll(dice: Dice) -> Generator[int, None, None]:
    """Generator containing random dice rolls"""
    return (random.randint(1, dice.sides) for _ in range(dice.number))


def parse(args: Tuple[str]) -> List[Union[str, int]]:
    """Substitutes dice rolls and splits 'sticky' operators."""
    return list(args)


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
        parse(args)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
