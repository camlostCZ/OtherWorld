from typing import Any, TextIO
from yaml import safe_load

from baseclasses import YAMLSourced


class ItemError(ValueError):
    pass


class OtherWorldItem(YAMLSourced):
    def __init__(self, id: str, name: str, title: str, description: str,
        weight: float) -> None:
        super().__init__()
        self.id: str = id
        self.name: str = name
        self.title: str = title
        self.description: str = description
        self.weight: float = weight
        self.flags: list[str] = []
        self.effects: dict[str, Any] = {}

