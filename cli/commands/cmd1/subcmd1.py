"""subcmd1"""

import argparse


def init_command(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--arg1",
        help="Arg1",
        required=True,
        choices=["val1", "val2"],
    )


def handle(args: argparse.Namespace) -> None:
    print(args)
