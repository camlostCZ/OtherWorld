from yaml import safe_load

from typing import TextIO

from inventory import OtherWorldInventory, InventoryItem
from baseclasses import YAMLSourced
from effect import Effect


class OtherWorldMap(YAMLSourced):
    """
    A map - class representing a single map in a world.
    """

    def __init__(self, id: str, title: str, description: str) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.exits = {}
        self.inventory = OtherWorldInventory("map_items")
        self.effects: list[Effect] = []
