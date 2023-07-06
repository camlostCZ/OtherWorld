from pathlib import Path
from typing import Generator, TypeVar

from map import OtherWorldMap
from item import OtherWorldItem
from baseclasses import YAMLSourced
from player import Player
from constants import (
    FILE_ENCODING,
    MAP_START,
)


YS = TypeVar('YS', bound=YAMLSourced)


class OtherWorldGame:
    def __init__(self):
        self.player = Player("Adventurer")
        self.items: dict[str, OtherWorldItem] = {}
        self.maps: dict[str, OtherWorldMap] = {}
        self.current_map: OtherWorldMap


    def load_items(self, path: str) -> None:
        """
        Load items from a directory.

        This method expects all YAML files in the directory contain
        a valid item specification. In case of error, exceptions
        are raised.

        Args:
            path (str): Path to a directory / folder.
        """
        for item in self._load_yaml_from_folder(path, OtherWorldItem):
            self.items[item.id] = item


    def load_maps(self, path: str) -> None:
        """
        Load maps from a directory.

        This method expects all YAML files in the directory contain
        a valid map specification. In case of error, exceptions
        are raised.

        Args:
            path (str): Path to a directory / folder.
        """
        for item in self._load_yaml_from_folder(path, OtherWorldMap):
            self.maps[item.id] = item

        self.current_map = self.maps[MAP_START]


    def _load_yaml_from_folder(self, path: str, cls: type[YS]) -> Generator[YS, None, None]:
        """
        Load game object from YAML files in a directory.

        The (private) method iterates over all YAML file in the directory
        specified by `path` and calls `load_yaml_file()` method of
        the class passed in `cls`.

        Args:
            path (str): Directory / folder path
            cls (type[YS]): Class name which instances should be loaded from the files

        Yields:
            Generator[YS, None, None]: Instance of the specified class
        """
        p = Path(path)
        for each in p.glob("*.yaml"):
            obj = cls()
            obj.load_yaml_file(each.open(encoding=FILE_ENCODING))
            yield obj
