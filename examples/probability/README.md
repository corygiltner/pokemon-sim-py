# Probability

An example using a random function called [choices](https://docs.python.org/3/library/random.html#functions-for-sequences). This function takes in a population list, a list of their respective weights and k a size of the list of elements choosen. 

## Explanation

First we need to import the random module

```python
import random
```

Next we create a class to define a Treasure item with two instance variables taking in a name and the weight of the rarity of the item. 

```python
class TreasureItem:
    def __init__(self, name="", rarity=0.0):
        self.name = name
        self.rarity = rarity
```

Let's create two items, one rare and one common with different weights. Their weights are floating point integers and should == 1. 

```python
rareTreasureItem = TreasureItem("rare", 0.2)

commonTreasureItem = TreasureItem("common", 0.8)
```

Next we have a TreasureChest class that can return one of the two items when it is opened. 

```python
class TreasureChest:
    def __init__(self):
        self.__ITEMS = [rareTreasureItem, commonTreasureItem]
        self.__ITEM_WEIGHTS = [rareTreasureItem.rarity, commonTreasureItem.rarity]

    def open(self):
        item = random.choices(population=self.__ITEMS, weights=self.__ITEM_WEIGHTS, k=1)
        return item[0]
```

The open method uses the choices function to randomly choose an item depending on their weight defined as their rarity. To test this out we can create two lists, one two hold the rare items picked and another to hold the common items picked. 

```python
rare_items = []
common_items = []
```

Next, we instantiate a TreasureChest and open the chest 10000 times adding the item to their corresponding list after it is found. 

```python
chest = TreasureChest()

for _ in range(0,10000):
    item = chest.open()
    if item.name == rareTreasureItem.name: 
        rare_items.append(item)
    elif item.name == commonTreasureItem.name: 
        common_items.append(item)
```

When the script runs, it will print the len of each of the item lists showing that the items are chosen very close to their weights. This is a random pick so the more iterations the open is executed the closer the distribution of the items will get to their weights. 

```bash
Number of Rare Items Found   : 1688
Number of Common Items Found : 8312
```
