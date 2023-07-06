from yaml import safe_load

from typing import TextIO

from inventory import OtherWorldInventory, InventoryItem
from baseclasses import YAMLSourced


class OtherWorldMap(YAMLSourced):
    """
    A map - class representing a single map in a world.
    """

    def __init__(self, game) -> None:
        self._game = game
        self.id = ""
        self.title = ""
        self.description = ""
        self.exits = {}
        self.items = OtherWorldInventory("map_items")


    def load_yaml_file(self, fd: TextIO) -> None:
        """
        Load a map from a YAML file

        Args:
            fd (TextIO): File descriptor of the source YAML file
        """
        data = safe_load(fd)
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]

        if "exits" in data:
            for item in data["exits"]:
                for key, val in item.items():
                    self.exits[key] = val

        if "items" in data:
            for item in data["items"]:
                id, count = item
                self.items.add_item(id, count)


    def to_string(self) -> str:
        """
        Create a readable text representation of a map.

        Returns:
            str: Human-readable map description.
        """
        items_str = ", ".join(
            [f"{self._game.items[x.id].title} ({x.count})" for x in self.items.items])
        exits_str = ", ".join(self.exits.keys())
        result = f"""{self.title}
{self.description}

  - Items: {items_str}
  - Possible exits: {exits_str}"""
        return result
