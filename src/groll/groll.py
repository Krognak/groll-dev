"""A helpful, dice rolling goblin for the command line!"""
import click

__version__ = "0.0.1"


@click.command()
@click.option("-v", "--version", is_flag=True)
def cli(**kwargs):
    """A helpful, dice rolling goblin for the command line!"""
    if "version" in kwargs:
        click.echo(f"groll v{__version__} - {__doc__}")


# pylint: disable=no-value-for-parameter,duplicate-code
if __name__ == "__main__":
    cli()
