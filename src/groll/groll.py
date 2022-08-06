"""A helpful, dice rolling goblin for the command line!"""

import operator
import random
import re
import sys

import click

from . import __version__

DICE_SYNTAX = r"\d*d\d+"

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


def roll(match):
    """roll dice strings of the form [n]d[s]"""
    num, sides = match.group(0).split("d")
    if not num:
        num = 1
    else:
        num = int(num)
    sides = int(sides)
    return sum((random.randint(1, sides) for _ in range(num)))


def str_to_int(args):
    """sub string representation of int with int"""
    subbed = []
    for arg in args:
        if arg:
            match = re.match(r"\d+", arg)
            if match:
                subbed.append(int(match.group(0)))
            else:
                subbed.append(arg)
    return subbed


def parse(dice):
    """parse dice input tuple into tuple of integers and operator strings"""
    if not dice:
        dstring = "1d20"
    else:
        dstring = " ".join(dice)
    dstring = re.sub(DICE_SYNTAX, roll, dstring)
    for strop in OPERATORS:
        pattern = "".join(("\\", strop))
        dstring = re.sub(pattern, f" {strop} ", dstring)
        dstring = re.sub(" +", " ", dstring)
    dstring = dstring.split()
    dstring = str_to_int(dstring)
    return dstring


def eval_maths(math_list):
    """evaluate maths safely from list"""
    if len(math_list) == 1:
        result = math_list[0]
    else:
        result, _operator, operand, *rest = math_list
        while rest:
            result = OPERATORS[_operator](result, operand)
            _operator, operand, *rest = rest
        result = OPERATORS[_operator](result, operand)
    return result


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
    result = eval_maths(parsed_string)
    click.echo(result)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
