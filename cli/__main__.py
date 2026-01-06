import argparse
import logging

from .commands import cmd1, cmd2, cmd3

logging.basicConfig(level=logging.INFO)

# This variable contains to all command packages
COMMAND_PACKAGES = [
    cmd1,
    cmd2,
    cmd3,
]
# This variable is a dictionary to store the command package to use it later for argpar parser creations and handlers
# The format is like the following:
#   "cmd1": (cmd1, <help_message_for_the_cmd1>)
COMMANDS = {m.__name__.split(".")[-1]: (m, m.__doc__) for m in COMMAND_PACKAGES}


def _init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command", required=True)
    for command_key, command_def in COMMANDS.items():
        command, help_text = command_def
        parser_cmd: argparse.ArgumentParser = subparsers.add_parser(
            command_key, help=help_text
        )
        command.init_command(parser_cmd)

    return parser


def main():
    _parser = _init_argparse()
    _args = _parser.parse_args()
    command_module = COMMANDS[_args.command][0]
    command_module.handle(_args)
