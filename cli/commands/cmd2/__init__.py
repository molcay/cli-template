"""cmd2 related commands. Example of dynamic command generation"""

import argparse

DYNAMIC_CMDS = {"dynamic1", "dynamic2"}

ACTIONS = {
    "subsubcmd1": ("Build the images for the given environment",),
    "subsubcmd2": (
        "Deploy the images and run the containers for the given environment",
    ),
}


def init_command(parser: argparse.ArgumentParser) -> None:
    subparsers = parser.add_subparsers(dest="subcommand", required=True)
    for dynamic_cmd in DYNAMIC_CMDS:
        parser = subparsers.add_parser(
            dynamic_cmd, help="dynamic parser for the given DYNAMIC_CMDS"
        )
        action_parser = parser.add_subparsers(dest="action", required=True)
        for action, (help_text, *_) in ACTIONS.items():
            action_parser.add_parser(action, help=help_text)


def handle(args: argparse.Namespace) -> None:
    print(args)
    env_name = args.subcommand
    action = args.action
    print(env_name, action)
