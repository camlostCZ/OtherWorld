from dataclasses import dataclass
from random import randint

@dataclass
class CharacterStats:
    hp: int = randint(4, 20)
    str: int = randint(1, 18)
    con: int = randint(1, 18)
    wis: int = randint(1, 18)
