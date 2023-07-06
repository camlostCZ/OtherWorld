from yaml import safe_load

from typing import TextIO

from inventory import OtherWorldInventory, InventoryItem
from baseclasses import YAMLSourced


class OtherWorldMap(YAMLSourced):
    """
    A map - class representing a single map in a world.
    """

    def __init__(self) -> None:
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
