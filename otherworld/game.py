from pathlib import Path

from map import OtherWorldMap
from item import OtherWorldItem
from player import Player
from constants import (
    FILE_ENCODING,
    MAP_START,
)

class OtherWorldGame:
    def __init__(self):
        self.player = Player("Adventurer")
        self.items: dict[str, OtherWorldItem] = {}
        self.maps: dict[str, OtherWorldMap] = {}
        self.current_map: OtherWorldMap


    def load_items(self, path: str) -> None:
        p = Path(path)
        for each_file in p.glob("*.yaml"):
            item = OtherWorldItem()
            item.load_yaml_file(each_file.open(encoding=FILE_ENCODING))
            self.items[item.id] = item


    def load_maps(self, path: str) -> None:
        p = Path(path)
        for each_file in p.glob("*.yaml"):
            # print(each_file)
            m = OtherWorldMap()
            m.load_yaml_file(each_file.open(encoding=FILE_ENCODING))
            self.maps[m.id] = m

        self.current_map = self.maps[MAP_START]
