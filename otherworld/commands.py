from cmdhandler import CommandHandler

# A dictionary of the available commands.
# Keep it sorted so that it's easy to locate individual commands.
COMMANDS = {
    "consume": {
        "help": "Eat an item if it's consumable",
        "pattern": r"^(?P<cmd>\w+)\s+(?P<code>[^\s]+)$",
        "fn": CommandHandler.cmd_consume
    },
    "drop": {
        "help": "Drop an item from player's inventory",
        "pattern": r"^(?P<cmd>\w+)\s+(?P<code>[^\s]+)$",
        "fn": CommandHandler.cmd_drop
    },
    "examine": {
        "help": "Examine an item in the player's inventory or on the current map",
        "pattern": r"^(?P<cmd>\w+)\s+(?P<code>[^\s]+)$",
        "fn": CommandHandler.cmd_examine
    },
    "go": {
        "help": "Go to another map using the specified direction",
        "pattern": r"^(?P<cmd>\w+)\s+(?P<exit>[^\s]+)$",
        "fn": CommandHandler.cmd_go
    },
    "inventory": {
        "help": "List the player's inventory",
        "fn": CommandHandler.cmd_inventory
    },
    "look": {
        "help": "Display a map description",
        "fn": CommandHandler.cmd_look
    },
    "quit": {
        "help": "Quit the game",
        "fn": CommandHandler.cmd_quit
    },
    "take": {
        "help": "Take an item from the floor / map",
        "pattern": r"^(?P<cmd>\w+)\s+(?P<code>[^\s]+)$",
        "fn": CommandHandler.cmd_take
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