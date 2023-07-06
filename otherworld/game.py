from pathlib import Path
from typing import Generator, Optional, TypeVar

from map import OtherWorldMap
from item import OtherWorldItem
from baseclasses import YAMLSourced
from inventory import OtherWorldInventory
from player import Player
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
        for item in self._load_yaml_from_folder(path, OtherWorldItem):
            self.items[item.id] = item


    def load_maps(self, path: str) -> None:
        """
        Load maps from a directory.

        This method expects all YAML files in the directory contain
        a valid map specification. In case of error, exceptions
        are raised.

        Args:
            path (str): Path to a directory / folder.
        """
        for item in self._load_yaml_from_folder(path, OtherWorldMap):
            self.maps[item.id] = item

        self.current_map = self.maps[MAP_START]


    def _load_yaml_from_folder(self, path: str, cls: type[YS]) -> Generator[YS, None, None]:
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
            obj = cls()
            obj.load_yaml_file(each.open(encoding=FILE_ENCODING))
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
        lines = []
        total_weight = 0.0
        if detailed:
            lines.append("      Id  Item name                                         Count  Weight")
        for idx, each in enumerate(inventory.items):
            item = self.items[each.id]
            item_code = OtherWorldInventory.CODE_SET[idx]
            title = item.title
            line = f"      {item_code:>{2}}. "
            if detailed:
                weight = each.count * item.weight
                total_weight += weight
                line += f"{title:<{48}}  {each.count:>{4}}  {weight:>{6}}"
            else:
                line += f"{title} ({each.count})"
            lines.append(line)
        if detailed:
            lines.append(f"Total item weight: {total_weight:.1f}")
        result = "\n".join(lines)
        return result
    

    def render_map(self, map_id: str) -> str:
        result = ""
        try:
            map = self.maps[map_id]
            items_str = self.render_inventory(map.items, detailed=False)
            exits_str = ", ".join(map.exits.keys())
            result = f"""{map.title}
{map.description}

  - Items: 
{items_str}
  - Possible exits: {exits_str}"""
        except KeyError:
            result = f"Error: Map ID '{map_id}' not found."
        return result
