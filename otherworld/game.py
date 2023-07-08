from pathlib import Path
from typing import Callable, Generator, Optional, TextIO, TypeVar

from yaml import safe_load

from map import OtherWorldMap
from item import OtherWorldItem, ItemError
from baseclasses import YAMLSourced
from inventory import InventoryError, OtherWorldInventory
from player import Player
from effect import Effect
from constants import (
    FILE_ENCODING,
    MAP_START,
)


YS = TypeVar('YS', bound=YAMLSourced)


class OtherWorldGame:
    def __init__(self):
        self.player = Player("Adventurer")
        self.items: dict[str, OtherWorldItem] = {}
        self.maps: dict[str, OtherWorldMap] = {}
        self.current_map: OtherWorldMap


    def load_items(self, path: str) -> None:
        """
        Load items from a directory.

        This method expects all YAML files in the directory contain
        a valid item specification. In case of error, exceptions
        are raised.

        Args:
            path (str): Path to a directory / folder.
        """
        for item in self._load_yaml_from_folder(path, self.load_item_from_yaml):
            self.items[item.id] = item


    def load_item_from_yaml(self, fd: TextIO) -> OtherWorldItem:
        """
        Load an item from a YAML file

        Args:
            fd (TextIO): File descriptor of the source YAML file

        Returns:
            OtherWorldItem: Item loaded from the file
        """
        data = safe_load(fd)
        item = OtherWorldItem(
            data["id"], data["name"], data["title"], data["description"],
            data["weight"])
        item.flags = data["flags"]

        if "effects" in data:
            for each in data["effects"]:
                try:
                    eff = Effect(each["name"], each["stat"], each["effect"], each["duration"])
                    item.effects.append(eff)
                except KeyError:
                    # Skip invalid records
                    pass
        return item


    def load_map_from_yaml(self, fd: TextIO) -> OtherWorldMap:
        """
        Load a map from a YAML file

        Args:
            fd (TextIO): File descriptor of the source YAML file

        Returns:
            OtherWorldMap: Map loaded from the file
        """
        data = safe_load(fd)
        map = OtherWorldMap(data["id"], data["title"], data["description"])

        if "exits" in data:
            for each in data["exits"]:
                for key, val in each.items():
                    map.exits[key] = val

        if "items" in data:
            for each in data["items"]:
                id, count = each
                item = self.items[id]
                map.inventory.add_item(item, count)

        if "effects" in data:
            for each in data["effects"]:
                try:
                    eff = Effect(each["name"], each["stat"], each["effect"], each["duration"])
                    map.effects.append(eff)
                except KeyError:
                    # Skip invalid records
                    pass
        return map


    def load_maps(self, path: str) -> None:
        """
        Load maps from a directory.

        This method expects all YAML files in the directory contain
        a valid map specification. In case of error, exceptions
        are raised.

        Args:
            path (str): Path to a directory / folder.
        """
        for item in self._load_yaml_from_folder(path, self.load_map_from_yaml):
            self.maps[item.id] = item

        self.current_map = self.maps[MAP_START]


    def _load_yaml_from_folder(self, path: str, fn: Callable) -> Generator[YS, None, None]:
        """
        Load game object from YAML files in a directory.

        The (private) method iterates over all YAML file in the directory
        specified by `path` and calls `load_yaml_file()` method of
        the class passed in `cls`.

        Args:
            path (str): Directory / folder path
            cls (type[YS]): Class name which instances should be loaded from the files

        Yields:
            Generator[YS, None, None]: Instance of the specified class
        """
        p = Path(path)
        for each in p.glob("*.yaml"):
            obj = fn(each.open(encoding=FILE_ENCODING))
            yield obj


    def item_name_to_id(self, item_name: str) -> Optional[str]:
        """
        Translate item name to item ID.

        Args:
            item_name (str): Name of an item

        Returns:
            Optional[str]: Item ID if found, None otherwise.
        """
        result = None
        for k, v in self.items.items():
            if v.name.lower() == item_name.lower():
                result = k
                break
        return result


    def render_inventory(self, inventory: OtherWorldInventory, detailed = False) -> str:
        """
        Render inventory string.
        There are two possible outputs - a simple one and a detailed one.
        The latter if `detailed` is True. The detailed one contains weight.

        Args:
            inventory (OtherWorldInventory): The inventory to render.
            detailed (bool, optional): If the detailed output should be rendered. Defaults to False.

        Returns:
            str: Rendered string (a fixed-width table)
        """
        lines = []
        total_weight = 0.0
        if detailed:
            lines.append("      Id  Item name                                         Count  Weight")
        for idx, each in enumerate(inventory.items):
            item = each.item
            item_code = OtherWorldInventory.CODE_SET[idx]
            line = f"      {item_code:>{2}}. "
            if detailed:
                weight = each.count * item.weight
                total_weight += weight
                line += f"{item.title:<{48}}  {each.count:>{4}}  {weight:>{6}}"
            else:
                line += f"{item.title} ({each.count})"
            lines.append(line)
        if detailed:
            lines.append(f"Total item weight: {total_weight:.1f}")
        result = "\n".join(lines)
        return result
    

    def render_map(self, map_id: str) -> str:
        """
        Render text map description. It's being displayed when the user
        enters the `look` command.

        Args:
            map_id (str): ID of the map to render.

        Returns:
            str: Rendered string
        """
        result = ""
        try:
            map = self.maps[map_id]

            items_table = ""
            items_str = self.render_inventory(map.inventory, detailed=False)
            if len(items_str) > 0:
                items_table = f"  - Items:\n{items_str}\n"

            exits_str = ", ".join(map.exits.keys())
            result = f"""{map.title}
{map.description}

{items_table}  - Possible exits: {exits_str}"""
        except KeyError:
            result = f"Error: Map ID '{map_id}' not found."
        return result


    def move_item_inv2inv(self, item_code: str, 
        source_inv: OtherWorldInventory, 
        target_inv: Optional[OtherWorldInventory] = None,
        flag: Optional[str] = None) -> None:
        """
        Move item from a source to a target inventory.
        Can be used to move item from map inventory to player's inventory
        and vice versa.
        If target_inv is None, item can be discarded or consumed.

        Args:
            item_code (str): Inventory code of an item
            source_inv (OtherWorldInventory): Source inventory
            target_inv (OtherWorldInventory): Target inventory
            flag (Optional[str]): Flag which has to be present on the item
                if the item should be moved

        Raises:
            ItemError: In case of non-matching flag
            InventoryError: Item cannot be moved, target inventory is full
        """
        inv_item = source_inv.get_item_by_code(item_code)
        if flag not in inv_item.item.flags:
            raise ItemError("Flag doesn't match.")
        
        try:
            if target_inv is not None:
                target_inv.add_item(inv_item.item)
            source_inv.remove_item(inv_item.item)
        except InventoryError:
            raise InventoryError("Item cannot be moved out of the source inventory.")
