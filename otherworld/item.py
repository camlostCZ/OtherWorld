from typing import Any, TextIO
from yaml import safe_load


class OtherWorldItem:
    id: str
    name: str
    title: str
    description: str
    weight: float
    properties: list[str]
    effects: dict[str, Any]

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
        self.properties = data["properties"]
        self.effects = data["effects"]
