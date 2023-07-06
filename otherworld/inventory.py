from item import OtherWorldItem

class InventoryError(RuntimeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InventoryItem:
    def __init__(self, id: str, count: int = 1):
        self.id = id
        #self.item: OtherWorldItem
        self.count = count

    def get_item_weight(self) -> float:
        return self.count * self.item.weight


class OtherWorldInventory:
    """
    Keeps an inventory of items.
    
    Used as player's inventory, player's equipment list,
    and list of items on a map.

    The game should use character codes ('a' .. 'z') to ease the selection
    of items from inventory. These codes are directly translatable to index
    - a -> 0, b -> 1, etc.
    """
    CODE_SET = [chr(ord('a') + x) for x in range(26)]

    def __init__(self, name: str, max_items: int = len(CODE_SET)) -> None:
        self.name = name
        self.max_items = max_items
        self.items: list[InventoryItem] = []


    def add_item(self, item_id: str, count: int = 1) -> None:
        """
        Add an item into the inventory.

        Args:
            item_id (str): Item ID

        Raises:
            InventoryError: In case of full inventory.
        """
        idx = self.get_item_idx(item_id)
        if idx >= 0:    # Item found
            self.items[idx].count += count
        elif len(self.items) < self.max_items:
            self.items.append(InventoryItem(item_id, count))
        else:
            raise InventoryError("Invetory full")


    def get_item_idx(self, item_id: str) -> int:
        """
        Search for item index in the inventory.

        Args:
            item_id (str): Item ID

        Returns:
            int: Index of the item in the inventory, or -1 if not found.
        """
        result = -1
        for idx, each in enumerate(self.items):
            if each.id == item_id:
                result = idx
                break
        return result


    def remove_item(self, item_id: str) -> None:
        """
        Remove an item from the inventory.

        Args:
            item_id (str): Item ID

        Raises:
            InventoryError: If the item is not present in the inventory.
        """
        idx = self.get_item_idx(item_id)
        if idx >= 0:    # Item found
            item = self.items[idx]
            item.count += -1
            if item.count == 0: # Last piece of an item removed
                self.items = self.items[:idx] + self.items[idx:]       
        else:
            raise InventoryError("Item not found")
        

    def get_item_idx_by_code(self, code: str) -> int:
        """
        Get item by so-called code which is typically a single letter.
        Can be overridden in child classes to increase the maximum capacity
        on inventories.

        Args:
            code (str): An item code

        Returns:
            int: Index translated from the code
        """
        idx = OtherWorldInventory.CODE_SET.index(code)
        return idx
