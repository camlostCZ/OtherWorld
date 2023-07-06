from typing import Any, TextIO
from yaml import safe_load

from baseclasses import YAMLSourced


class OtherWorldItem(YAMLSourced):
    def __init__(self) -> None:
        super().__init__()
        self.id: str
        self.name: str
        self.title: str
        self.description: str
        self.weight: float
        self.flags: list[str]
        self.effects: dict[str, Any]
        

    def load_yaml_file(self, fd: TextIO) -> None:
        """
        Load a map from a YAML file

        Args:
            fd (TextIO): File descriptor of the source YAML file
        """
        data = safe_load(fd)
        self.id = data["id"]
        self.name = data["name"]
        self.title = data["title"]
        self.description = data["description"]
        self.weight = data["weight"]
        self.flags = data["flags"]
        self.effects = data["effects"]
