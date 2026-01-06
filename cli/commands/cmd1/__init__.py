"""cmd1 related commands"""

import argparse

from . import subcmd1

SUBCOMMANDS = {
    "subcmd1": subcmd1,
}


def init_command(parser: argparse.ArgumentParser) -> None:
    subparsers = parser.add_subparsers(dest="subcommand", required=True)
    for subcommand_key, subcommand_package in SUBCOMMANDS.items():
        parser = subparsers.add_parser(subcommand_key, help=subcommand_package.__doc__)
        subcommand_package.init_command(parser)


def handle(args: argparse.Namespace) -> None:
    SUBCOMMANDS[args.subcommand].handle(args)
