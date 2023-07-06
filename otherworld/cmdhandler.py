from map import OtherWorldMap
from game import OtherWorldGame
from player import Player


class CommandHandler:
    @classmethod
    def cmd_eat(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        msg = "This item cannot be eaten."
        parts = cmd.split(" ")
        if len(parts) == 2:
            item_name = parts[-1]
            inventory = game.player.inventory
        else:
             msg = "Error: Use `eat <inventory item id>` to eat an item."
        return (msg, False)


    @classmethod
    def cmd_go(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        msg = ""
        parts = cmd.split(" ")
        if len(parts) == 2:
            exit_name = parts[-1]
            if exit_name in game.current_map.exits:
                id = game.current_map.exits[exit_name]
                if id in game.maps:
                    game.current_map = game.maps[id]
                else:
                    msg = "Error: Map not available."
            else:
                msg = "Error: Unknown exit"
        else:
            msg = "Error: Use `go <exit name>` to move in the game."
        return(msg, False)


    @classmethod
    def cmd_inventory(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        msg = "Your inventory is empty."
        if len(game.player.inventory.items) > 0:
            inv_str = game.render_inventory(game.player.inventory, detailed=True)
            msg = f"Your inventory contains these items:\n{inv_str}"
        return (msg, False)
    

    @classmethod
    def cmd_look(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        map_str = game.render_map(game.current_map.id)
        return (map_str, False)
    

    @classmethod
    def cmd_quit(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        return ("Exiting the game.", True)
    

    @classmethod
    def cmd_take(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        msg = "Error: Use `take <item id>` to take items."
        parts = cmd.split(" ", maxsplit=1)
        if len(parts) == 2:
            # TODO Search for an item in the current map.
            # If not found, report an error.
            # If not collectable, report an error.
            # Otherwise:
            #   - remove the item from map inventory
            #   - add the item to player's inventory
            pass
        return (msg, False)
