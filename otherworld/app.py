import sys

from pathlib import Path

from constants import PATH_ITEMS, PATH_MAPS
from commands import COMMANDS, CMD_ALIASES
from game import OtherWorldGame


class CliApp:
    def __init__(self) -> None:
        self.game: OtherWorldGame = OtherWorldGame()
        self.game.load_items(PATH_ITEMS)
        self.game.load_maps(PATH_MAPS)


    def cmd_help_handler(self):
        print("Available commands:")
        for k, v in COMMANDS.items():
            print(f"    {k:<{16}}{v['help']}")


    def handle_cmd(self, cmd: str) -> tuple[str, bool]:
        msg = "Unknown command. See help."
        should_exit = False
        try:
            key = cmd.split(" ")[0]
            cmd_name = CMD_ALIASES[key]
            command = COMMANDS[cmd_name]
            msg, should_exit = command["fn"](cmd, self.game)
        except KeyError as e:
            msg = "Error: Unknown command."
        return (msg, should_exit)


    def run(self) -> None:
        try:
            finished = False
            while not finished:
                print(f"\nYou are here:  {self.game.current_map.title}")
                cmd = input("\nEnter command: ").lower()
                print()

                if cmd in "help,h,?".split(","):
                    self.cmd_help_handler()
                else:
                    msg, finished = self.handle_cmd(cmd)
                    print(msg)
        except KeyError as e:
            print(f"Error: Invalid map specified. No maps found?", file=sys.stderr)
