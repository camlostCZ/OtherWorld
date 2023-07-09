from charproperties import CharacterStats
from inventory import OtherWorldInventory
from effect import Effect


class Player:
    """
    Class representing a single player.
    A player has a name, several properties, some equipment, 
    and an inventory of items.
    """

    def __init__(self, name: str):
        self.name = name
        self.title = ""
        self.stats = CharacterStats()
        self.inventory = OtherWorldInventory("player's inventory")
        self.effects: list[Effect] = [
            #Effect(name="poison", stat="hp", effect=-3, duration=5)
        ]   # Intended for spells, poisons, etc.
        self.current_inventory = self.inventory # Used by `examine` command


    def apply_effects(self) -> tuple[str, bool]:
        """
        Apply all the active effects on the player.

        Returns:
            str: A tuple of message displayed to the user and a boolean flag
                indicating if the game should finish (True).
        """
        msgs = []
        for each in self.effects:
            self.stats = each.modify_stats(self.stats)
            msgs.append(f"You're under effect of {each.name}. Your {each.stat_affected} has changed by {each.stat_effect}.")
            each.duration += -1

        # Remove effects with exhausted duration
        self.effects = [x for x in self.effects if x.duration > 0]

        finished = self.stats.hp <= 0
        if finished:
            msgs.append("You've died. Be more careful next time.")
        msg = "\n".join(msgs)
        return (msg, finished)


    