# pylint: disable=missing-module-docstring
import sys

from .groll import cli

cli(sys.argv[1:])
