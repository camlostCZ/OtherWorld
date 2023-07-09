from typing import Callable
from game import OtherWorldGame

# A dictionary of the available commands.
# Keep it sorted so that it's easy to locate individual commands.
COMMANDS = {
    "consume": {
        "help": "Eat an item if it's consumable",
        "usage": "Use `consume <inventory item code>` to consume an item.",
        "pattern": r"^(?P<cmd>\w+)\s+(?P<code>[^\s]+)$",
    },
    "drop": {
        "help": "Drop an item from player's inventory",
        "usage": "Use `drop <item code>` to drop an item.",
        "pattern": r"^(?P<cmd>\w+)\s+(?P<code>[^\s]+)$",
    },
    "examine": {
        "help": "Examine an item in the player's inventory or on the current map",
        "usage": "Use `examine <item code>` to examine an item.",
        "pattern": r"^(?P<cmd>\w+)\s+(?P<code>[^\s]+)$",
    },
    "go": {
        "help": "Go to another map using the specified direction",
        "usage": "Use `go <exit name>` to move in the game.",
        "pattern": r"^(?P<cmd>\w+)\s+(?P<exit>[^\s]+)$",
    },
    "inventory": {
        "help": "List the player's inventory",
        "usage": "",
        "pattern": r"^(?P<cmd>\w+)$",
    },
    "look": {
        "help": "Display a map description",
        "usage": "",
        "pattern": r"^(?P<cmd>\w+)$",
    },
    "quit": {
        "help": "Quit the game",
        "usage": "",
        "pattern": r"^(?P<cmd>\w+)$",
    },
    "take": {
        "help": "Take an item from the floor / map",
        "usage": "Use `take <item code>` to take items.",
        "pattern": r"^(?P<cmd>\w+)\s+(?P<code>[^\s]+)$",
    }
}

# A dictionary for alias -> command mappings.
# The program uses this dictionary to search for commands.
CMD_ALIASES = {
    "c": "consume",
    "consume": "consume",
    "d": "drop",
    "drop": "drop",
    "ex": "examine",
    "examine": "examine",
    "g": "go",
    "go": "go",
    "i": "inventory",
    "inv": "inventory",
    "inventory": "inventory",
    "l": "look",
    "look": "look",
    "q": "quit",
    "quit": "quit",
    "t": "take",
    "take": "take"
}

def get_cmd_handler(cmd: str, game: OtherWorldGame) -> Callable:
    """
    Provide mapping of commands to their handlers.

    Using the COMMANDS dictionary for the mapping lead to
    circular dependencies in case of some commands, thus the function.

    Args:
        cmd (str): Commands name
        game (OtherWorldGame): The game object - used to modify game state.

    Returns:
        Callable: A OtherWorldGame method designed to handle the command.
    """
    match cmd:
        case "consume":
            return game.handle_cmd_consume
        case "drop":
            return game.handle_cmd_drop
        case "examine":
            return game.handle_cmd_examine
        case "go":
            return game.handle_cmd_go
        case "inventory":
            return game.handle_cmd_inventory
        case "look":
            return game.handle_cmd_look
        case "quit":
            return game.handle_cmd_quit
        case "take":
            return game.handle_cmd_take
