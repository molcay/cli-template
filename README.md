# CLI Template

This is a template for a command-line interface (CLI) application written in Python.
This will mostly be used as a starting point for creating new CLI applications.

The key aspect of this template is that there is no external dependencies.

It is designed to be simple and easy to understand.

I also tend to use this template to create CLI for other on-going projects as a replacement of bash scripts and Makefile (or any alternatives).
For example, I have used this template to create a CLI for my Django application to interact with the other tools like `docker`, `python manage.py`, etc.

The `cli` folder contains the following files:
- `__main__.py`: This is the entry point for the CLI application.
- `commands`: This folder contains all the command packages.
- `commands/cmd1`: A command package to give a glimpse of how you can use folder structure to create a command with subcommands and arguments.
- `commands/cmd2`: Another example package to explain how to create a dynamic subcommands.
- `commands/cmd3`: Bare minimum package. The main purpose is to demonstrate how to create a command for this documentation.

# Usage:
- You can download the `cli` folder and put it in your project directory (I suggest you put it in the root of your project). Since it contains some examples, you can use it as a starting point for your own CLI application.

- You also need to add the following to your `pyproject.toml` file:
```toml
# if the build system is not set, you need to add the following lines:
[build-system]
requires = ["setuptools>=80.9.0", "wheel"]
build-backend = "setuptools.build_meta"

# Add the following lines to be able to run the CLI application in this format: `cli cmd1 subcmd2 --arg1 value1` without using python executable.
[project.scripts]
cli = "cli.__main__:main"
```

- After adding the previous lines, you can run `uv sync` command install the cli in your virtual environment in editable mode.
- If you completed the previous steps, you can run `cli --help` command to see the help message.
```shell
usage: cli [-h] {cmd1,cmd2} ...

positional arguments:
  {cmd1,cmd2}
    cmd1       cmd1 related commands
    cmd2       cmd2 related commands. Example of dynamic command generation

options:
  -h, --help   show this help message and exit
```

## How to add a new command:
 To be able to add a new command follow these steps;
 1. Create a **package** folder[^1] in the `commands` folder. (e.g. `cmd3`)
 2. Add a doc string for the `__init__` file. This doc string will be used in help message.
 3. Create `init_command` function inside the `__init__` file. With this function you can define arguments, subcommands, etc. The signature for the init_command function:
 ```Python
 def init_command(parser: argparse.ArgumentParser) -> None:
 ```
 4. Create "handle" function inside the `__init__` file. In this function you need to handle the logic for the command. The signature for the `handle` function:
 ```Python
 def handle(parser: argparse.ArgumentParser) -> None:
 ```
 5. Import the new package into the `cli/__main__.py` file. The import statement needs to follow the following format:
 ```Python
 from .commands import <newpackage>  # e.g. from .commands import cmd3
 ```
> Please change the `<newpackage>` to the name of the package folder that you created in the step #1.

 6. Add `<newpackage>` to the `COMMAND_PACKAGES` list.
 ```python
 from .commands import cmd3  # ----> new line
 # ...
 COMMAND_PACKAGES = [
     # ...,
     cmd3,  # ----> new line
 ]
 ```
 
 7. After adding the new package to the `COMMAND_PACKAGES` list, you can now use the new command. Here is the expected output for the `cli --help` command:
 ```shell
 $ cli --help
 usage: cli [-h] {cmd1,cmd2,cmd3} ...
 
 positional arguments:
   {cmd1,cmd2,cmd3}
     cmd1            cmd1 related commands
     cmd2            cmd2 related commands. Example of dynamic command generation
     cmd3            Command 3 docs
 
 options:
   -h, --help        show this help message and exit
 ```

[^1]: **package** folder means a folder that contains `__init__.py` file.

> To add a subcommand, please check the `__init__` file of the example implementations.
