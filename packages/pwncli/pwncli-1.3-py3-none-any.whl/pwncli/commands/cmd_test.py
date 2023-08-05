import click
import sys
from pwncli.cli import pass_environ


@click.command(name='test', short_help="Test command.")
@click.option('-v', '--verbose', count=True, show_default=True, help="Show more info or not.")
@pass_environ
def cli(ctx, verbose):
    print("test...", verbose)
    pass