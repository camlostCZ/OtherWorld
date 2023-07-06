from cmdhandler import CommandHandler

# A dictionary of the available commands.
# Keep it sorted so that it's easy to locate individual commands.
COMMANDS = {
    "eat": {
        "help": "Eat an item if it's to eat.",
        "fn": CommandHandler.cmd_eat
    },
    "go": {
        "help": "Go to another map using the specified direction",
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
        "fn": CommandHandler.cmd_take
    }
}

CMD_ALIASES = {
    "eat": "eat",
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