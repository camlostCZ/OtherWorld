from charproperties import CharacterStats


class Effect:
    """
    Effect is an influence on the player's character.

    It affects their stats in either positive or negative way
    for a limited duration (i.e. moves).

    Example:
      Poisonous mushroom with effect ["hp", -2, 10] will
      decrease player's HP by 2 every move for 10 moves.

    There can be several effects affecting the player at the same
    time.
    """
    def __init__(self, name: str, stat: str, effect: int, duration: int) -> None:
        self.name: str = name
        self.description: str
        self.stat_affected: str = stat
        self.stat_effect: int = effect
        self.duration: int = duration


    def modify_stats(self, stats: CharacterStats) -> CharacterStats:
        match self.stat_affected:
            case "hp":
                stats.hp += self.stat_effect
        return stats