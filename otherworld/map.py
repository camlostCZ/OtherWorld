from yaml import safe_load

from typing import TextIO

from inventory import InventoryItem
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
        self.items: list[InventoryItem] = []


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
        for item in data["exits"]:
            for key, val in item.items():
                self.exits[key] = val

        for item in data["items"]:
            id, count = item
            inv_item = InventoryItem()


    def to_string(self) -> str:
        """
        Create a readable text representation of a map.

        Returns:
            str: Human-readable map description.
        """
        result = f"{self.title}\n\n{self.description}\n\nExits:\n"
        for key, val in self.exits.items():
            result += f"  - {key}\n"
        return result
