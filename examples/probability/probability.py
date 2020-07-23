import random

class TreasureItem:
    def __init__(self, name="", rarity=0.0):
        self.name = name
        self.rarity = rarity

rareTreasureItem = TreasureItem("rare", 0.2)

commonTreasureItem = TreasureItem("common", 1.0)

class TreasureChest:
    def __init__(self):
        self.__ITEMS = [rareTreasureItem, commonTreasureItem]
        self.__ITEM_WEIGHTS = [rareTreasureItem.rarity, commonTreasureItem.rarity]

    def open(self):
        item = random.choices(population=self.__ITEMS, weights=self.__ITEM_WEIGHTS, k=1)
        return item[0]

rare_items = []
common_items = []

chest = TreasureChest()

for _ in range(0,10000):
    item = chest.open()
    if item.name == rareTreasureItem.name: 
        rare_items.append(item)
    elif item.name == commonTreasureItem.name: 
        common_items.append(item)

rare_len = len(rare_items)
common_len = len(common_items)

print(f"Number of Rare Items Found   : {rare_len}")
print(f"Number of Common Items Found : {common_len}")