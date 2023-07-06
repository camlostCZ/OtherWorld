from map import OtherWorldMap
from game import OtherWorldGame
from inventory import InventoryError
from constants import FLAG_COLLECTABLE, FLAG_CONSUMABLE
from player import Player


class CommandHandler:
    """
    Class to keep all command handlers together. It also allows for an
    easy import.

    Each command handler is a class method with the following parameters:
        - cmd: Command string as enterer by the user.
        - game: The OtherWorldGame object. Used to access game data.
    Command handlers return a tuple of string displayed to the user 
    (response to the command) and a flag idicating the game should end.
    """
    
    @classmethod
    def cmd_consume(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        msg = "This item cannot be consumed."
        parts = cmd.split(" ")
        if len(parts) == 2:
            code = parts[-1].strip()
            inventory = game.player.inventory
            item_idx = inventory.get_item_idx_by_code(code)
            try:
                item_id = inventory.items[item_idx].id
                # FIXME Possible bug if item_id wrong? Can it happen?
                item = game.items[item_id]
                # If not collectable, report an error.
                if FLAG_CONSUMABLE in item.flags:
                    inventory.remove_item(item_id)
                    msg = f"You've consumed {item.name}."
                    # TODO Remove some amount of hunger
                    # TODO Apply effects if any present on the item
                else:
                    msg = "This item cannot be consumed."
            except IndexError as e:
                # If not found, report an error.
                msg = "Cannot consume an item. No such item available."
            except InventoryError as e:
                msg = e
        else:
             msg = "Error: Use `consume <inventory item code>` to consume an item."
        return (msg, False)


    @classmethod
    def cmd_examine(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        msg = "Error: Use `examine <item code>` to examine an item."
        parts = cmd.split(" ")
        if len(parts) == 2:
            code = parts[-1].strip()
            inventory = game.player.current_inventory
            item_idx = inventory.get_item_idx_by_code(code)
            try:
                item_id = inventory.items[item_idx].id
                # FIXME Possible bug if item_id wrong? Can it happen?
                item = game.items[item_id]
                msg = item.description
            except IndexError:
                msg = "No such item."
        return (msg, False)


    @classmethod
    def cmd_go(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        msg = ""
        parts = cmd.split(" ")
        if len(parts) == 2:
            exit_name = parts[-1].strip()
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

        # Reset the current inventory to the player's one (for the `examine` command)
        game.player.current_inventory = game.player.inventory

        return(msg, False)


    @classmethod
    def cmd_inventory(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        msg = "Your inventory is empty."
        if len(game.player.inventory.items) > 0:
            inv_str = game.render_inventory(game.player.inventory, detailed=True)
            msg = f"Your inventory contains these items:\n{inv_str}"

        # Set the current inventory to the player's one (for the `examine` command)
        game.player.current_inventory = game.player.inventory

        return (msg, False)
    

    @classmethod
    def cmd_look(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        map_str = game.render_map(game.current_map.id)

        # Set the map's inventory as the current for the `examine` command
        game.player.current_inventory = game.current_map.items

        return (map_str, False)
    

    @classmethod
    def cmd_quit(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        return ("Exiting the game.", True)
    

    @classmethod
    def cmd_take(cls, cmd: str, game: OtherWorldGame) -> tuple[str, bool]:
        msg = "Error: Use `take <item code>` to take items."
        parts = cmd.split(" ", maxsplit=1)
        if len(parts) == 2:
            # Search for an item in the current map.
            code = parts[1].strip()
            inventory = game.current_map.items
            item_idx = inventory.get_item_idx_by_code(code)
            try:
                item_id = inventory.items[item_idx].id
                # FIXME Possible bug if item_id wrong? Can it happen?
                item = game.items[item_id]
                # If not collectable, report an error.
                if FLAG_COLLECTABLE in item.flags:
                    inventory.remove_item(item_id)
                    game.player.inventory.add_item(item_id)
                    msg = f"You've taken {item.name}."
                else:
                    msg = "This item cannot be taken."
            except IndexError as e:
                # If not found, report an error.
                msg = "Cannot take an item. No such item available."
            except InventoryError as e:
                msg = e
        
        return (msg, False)
