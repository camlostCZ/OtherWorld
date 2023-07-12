from dataclasses import dataclass
from random import randint

@dataclass
class CharacterStats:
    # FIXME The stats should be initialized with wome reasonable values.
    max_hp: int = randint(4, 20)
    hp: int = max_hp
    attack: int = randint(0, 10)
    defense: int = randint(0, 5)

    # The relation between HP, attack and defense:
    # During battle:
    #   if attack > defense: 
    #     HP = HP - ( attack - defense )
