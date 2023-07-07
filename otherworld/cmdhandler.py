from map import OtherWorldMap
from game import OtherWorldGame
from inventory import InventoryError
from constants import FLAG_COLLECTABLE, FLAG_CONSUMABLE
from effect import Effect
from item import ItemError
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
    def cmd_consume(cls, cmd_dict: dict[str, str], game: OtherWorldGame) -> tuple[str, bool]:
        msg = "This item cannot be consumed."
        try:
            inventory = game.player.inventory
            item = inventory.get_item_by_code(cmd_dict["code"]).item
            # If not collectable, report an error.
            if FLAG_CONSUMABLE in item.flags:
                inventory.remove_item(item)
                msg = f"You've consumed {item.name}."
                # Apply effects if any present on the item
                for each in item.effects:
                    eff = Effect(each["name"], each["stat"], each["effect"], each["duration"])
                    game.player.effects.append(eff)
            else:
                msg = "This item cannot be consumed."
        except IndexError as e:
            # If not found, report an error.
            msg = "Cannot consume an item. No such item available."
        except InventoryError as e:
            msg = f"{e}"
        return (msg, False)
    

    @classmethod
    def cmd_drop(cls, cmd_dict: dict[str, str], game: OtherWorldGame) -> tuple[str, bool]:
        try:
            game.move_item_inv2inv(cmd_dict["code"], game.player.inventory, game.current_map.inventory)
            msg = f"The item has been dropped from your inventory."
        except InventoryError as e:
            msg = f"{e}"
        return (msg, False)


    @classmethod
    def cmd_examine(cls, cmd_dict: dict[str, str], game: OtherWorldGame) -> tuple[str, bool]:
        try:
            inventory = game.player.current_inventory
            item = inventory.get_item_by_code(cmd_dict["code"]).item
            msg = item.description
        except IndexError:
            msg = "No such item."
        return (msg, False)


    @classmethod
    def cmd_go(cls, cmd_dict: dict[str, str], game: OtherWorldGame) -> tuple[str, bool]:
        msg = ""
        exit_name = cmd_dict["exit"]
        if exit_name in game.current_map.exits:
            id = game.current_map.exits[exit_name]
            if id in game.maps:
                game.current_map = game.maps[id]
                for each in game.current_map.effects:
                    game.player.effects.append(each)

                msg = f"You are here: {game.current_map.title}"
            else:
                msg = "Error: Map not available."
        else:
            msg = "Error: Unknown exit"

        # Reset the current inventory to the player's one (for the `examine` command)
        game.player.current_inventory = game.player.inventory

        return(msg, False)


    @classmethod
    def cmd_inventory(cls, cmd_dict: dict[str, str], game: OtherWorldGame) -> tuple[str, bool]:
        msg = "Your inventory is empty."
        if len(game.player.inventory.items) > 0:
            inv_str = game.render_inventory(game.player.inventory, detailed=True)
            msg = f"Your inventory contains these items:\n{inv_str}"

        # Set the current inventory to the player's one (for the `examine` command)
        game.player.current_inventory = game.player.inventory

        return (msg, False)
    

    @classmethod
    def cmd_look(cls, cmd_dict: dict[str, str], game: OtherWorldGame) -> tuple[str, bool]:
        map_str = game.render_map(game.current_map.id)

        # Set the map's inventory as the current for the `examine` command
        game.player.current_inventory = game.current_map.inventory

        return (map_str, False)
    

    @classmethod
    def cmd_quit(cls, cmd_dict: dict[str, str], game: OtherWorldGame) -> tuple[str, bool]:
        return ("Exiting the game.", True)
    

    @classmethod
    def cmd_take(cls, cmd_dict: dict[str, str], game: OtherWorldGame) -> tuple[str, bool]:
        try:
            code = cmd_dict["code"]
            item = game.current_map.inventory.get_item_by_code(code).item
            game.move_item_inv2inv(code, 
                game.current_map.inventory, game.player.inventory, 
                flag=FLAG_COLLECTABLE)
            msg = f"You've taken {item.name}."
        except ItemError:
            msg = "This item cannot be taken."
        except IndexError as e:
            # If not found, report an error.
            msg = "Cannot take an item. No such item available."
        except InventoryError as e:
            msg = e
        
        return (msg, False)
