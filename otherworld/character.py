from inventory import OtherWorldInventory
from charproperties import CharacterStats
from effect import Effect


class Character:
    """
    A parent class to all characters in the game, i.e. for NPCs and players.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.inventory: OtherWorldInventory = OtherWorldInventory("character's inventory")
        self.stats: CharacterStats = CharacterStats()
        self.money = 0
        self.effects: list[Effect] = []   # Intended for spells, poisons, etc.


    def apply_effects(self) -> tuple[str, bool]:
        """
        Apply all the active effects on the character.

        Returns:
            str: A tuple of message displayed to the user and a boolean flag
                indicating if the game should finish (True).
        """
        msgs = []
        for each in self.effects:
            self.stats = each.modify_stats(self.stats)
            msgs.append(f"{self.name} is under effect of {each.name} - {each.stat_affected} changed by {each.stat_effect}.")
            each.duration += -1

        # Remove effects with exhausted duration
        self.effects = [x for x in self.effects if x.duration > 0]

        finished = self.stats.hp <= 0
        if finished:
            msgs.append(f"{self.name} died.")
        msg = "\n".join(msgs)
        return (msg, finished)
    

class NPC(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.is_dead = False
        self.home: str  # Map ID
        self.distance_from_home = 0