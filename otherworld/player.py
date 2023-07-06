from charproperties import CharacterProperties
from inventory import InventoryItem


class Player:
    """
    Class representing a single player.
    A player has a name, several properties, some equipment, 
    and an inventory of items.
    """

    def __init__(self, name: str):
        self.name = name
        self.title = ""
        self.properties = CharacterProperties()
        self.inventory: list[InventoryItem] = []
        self.effects = []   # Intended for spells, poisons, etc.


    def get_total_item_weight(self) -> float:
        return sum((x.get_item_weight() for x in self.inventory))
    