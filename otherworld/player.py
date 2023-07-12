from charproperties import CharacterStats
from inventory import OtherWorldInventory
from effect import Effect
from character import Character


class Player(Character):
    """
    Class representing a single player.
    A player has a name, several properties, some equipment, 
    and an inventory of items.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.level = 1
        self.current_inventory = self.inventory # Used by `examine` command
