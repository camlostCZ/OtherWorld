import re
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
        """
        Handle user commands.


        Args:
            cmd (str): String command as entered by the user

        Returns:
            tuple[str, bool]: A tuple of command response (message) and
                a flag indicating the game should finish.
        """
        msg = "Unknown command. See help."
        should_exit = False
        try:
            key = cmd.split(" ")[0]
            cmd_name = CMD_ALIASES[key]
            command = COMMANDS[cmd_name]
            m = re.match(command["pattern"], cmd)
            if m:
                msg, should_exit = command["fn"](m.groupdict(), self.game)
            else:
                msg = f"Error: {command['usage']}"
        except KeyError as e:
            msg = "Error: Unknown command."
        return (msg, should_exit)


    def run(self) -> None:
        """
        Main loop. This is where the commands are handled.
        """
        try:
            finished = False
            msg = f"\nYou are here:  {self.game.current_map.title}"
            while True:
                if msg:
                    print(f"\n{msg}")

                msg, death = self.game.player.apply_effects()
                if msg:
                    print(f"\n{msg}")
                finished = finished or death

                if finished or death:
                    break

                cmd = input(f"\n[HP: {self.game.player.stats.hp}]  Your action: ").lower()
                print()

                if cmd in "help,h,?".split(","):
                    self.cmd_help_handler()
                else:
                    msg, finished = self.handle_cmd(cmd)                        
        except KeyError as e:
            print(f"Error: Invalid map specified. No maps found?", file=sys.stderr)
