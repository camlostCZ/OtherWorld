from item import OtherWorldItem

class InventoryItem:
    def __init__(self):
        self.id: str
        self.item: OtherWorldItem
        self.count: int = 1

    def get_item_weight(self) -> float:
        return self.count * self.item.weight


class OtherWorldInventory:
    """
    Keeps an inventory of items. 
    
    Used as player's inventory, player's equipment list,
    and list of items on a map.
    """

    def __init__(self, max_items: int) -> None:
        self.max_items = max_items
        self.items: dict[str, InventoryItem] = {}


    def add_item(self, item_name: str) -> None:
        # TODO Add an item to the inventory
        # i.e. assign a key and add it to the dict.
        pass


    def get_item(self, id: str) -> InventoryItem:
        # TODO Return an InventoryItem object from the inventory
        pass


    def remove_item(self, id: str) -> None:
        # TODO Remove an item from inventory
        pass