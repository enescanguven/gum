from pyfiglet import figlet_format
from termcolor import cprint
import argparse


class Command:
    def execute(self):
        raise NotImplementedError("You should implement this method in your subclass")


class Gum(Command):
    def execute(self):
        ascii_art = figlet_format("Chewing GUM", font="bulbhead", width=200)
        cprint(ascii_art, "yellow", attrs=["bold"])
        cprint(
            "Welcome to GUM - the command line tool to switch between git users.",
            "white",
            attrs=["bold"],
        )


class CreateUser(Command):
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def execute(self):
        print(f"Creating a user with username: {self.username} and email: {self.email}")


class SwitchUser(Command):
    def __init__(self, username):
        self.username = username

    def execute(self):
        print(f"Switching to user: {self.username}")


class DeleteUser(Command):
    def __init__(self, username):
        self.username = username

    def execute(self):
        print(f"Deleting user: {self.username}")


class Help(Command):
    def execute(self):
        ascii_art = figlet_format("GUM", font="bulbhead", width=200)
        cprint(ascii_art, "yellow", attrs=["bold"])
        cprint("Introduction:", "yellow", attrs=["bold"])
        cprint(
            "Welcome to GUM - the command line tool to switch between git users.",
            "white",
            attrs=["bold"],
        )
        print("Chewing gum")
        command_list = {
            "gum": "Main command",
            "use": "Switch between git users",
            "create": "Create a new git user",
            "delete": "Delete a git user",
        }
        print("Available commands:")
        for command, description in command_list.items():
            print(f"{command}: {description}")

        print("Usage:")

        usage_list = {
            "gum": "gum",
            "use": "gum use <username>",
            "create": "gum create <username> <email>",
            "delete": "gum delete <username>",
        }

        for command, usage in usage_list.items():
            print(f"{command}: {usage}")

        print("For more information, visit enescanguven.com/gum")


class GumRoot:
    def __init__(self):
        self.__parse_args()

    def __parse_args(self):
        parser = argparse.ArgumentParser(prog="gum", add_help=False)

        sub_parsers = parser.add_subparsers(dest="command")

        gum_parser = sub_parsers.add_parser("gum", help="gum command")
        gum_parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")

        help_parser = sub_parsers.add_parser("help", help="help command")
        help_parser.add_argument(
            "command", nargs="?", type=str, help="command to get help for"
        )

        use_parser = sub_parsers.add_parser("use", help="use command")
        use_parser.add_argument("username", type=str, help="username to switch to")

        create_parser = sub_parsers.add_parser("create", help="create command")
        create_parser.add_argument("username", type=str, help="username to create")
        create_parser.add_argument("email", type=str, help="email to create")

        delete_parser = sub_parsers.add_parser("delete", help="delete command")
        delete_parser.add_argument("username", type=str, help="username to delete")

        args = parser.parse_args()
        command_args = vars(args)
        command = command_args.pop("command")
        command_class = self._get_command_class(command)
        command_instance = command_class(**command_args)
        command_instance.execute()

    def _get_command_class(self, command: str):
        commands = {
            None: Gum,
            "use": SwitchUser,
            "create": CreateUser,
            "delete": DeleteUser,
            "help": Help,
        }
        return commands[command]

    def execute(self, command):
        if command in self.commands:
            self.commands[command].execute()
        else:
            print(
                f"Command '{command}' not found. Please use 'gum help' to see available commands."
            )


def main():
    GumRoot()
