from charproperties import CharacterProperties
from inventory import InventoryItem, OtherWorldInventory


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
        self.inventory = OtherWorldInventory("player's inventory")
        self.effects = []   # Intended for spells, poisons, etc.


    