'''
   Knuth Shuffle Algorithm is simple way to shuffle items around in the list.
   Algorithm can shuffle any types of items: numbers, strings, images.
   Algorithm doesn't need extra space for items to shuffle, instead is uses the space
   inside the list itself.
   1. Create pointer "i" on the last item of the list
   2. This has effect of dividing the list in two parts:
   - right part represents shuffled items, initially empty - no items.
   - left part represents not shuffled items.
   4. Select a random item from not shuffled items, and swap with item at position index "i".
   5. After swap move "i" one position to the left i=n-2
   - shuffled part - grows by one item
   - not shuffled part - shrinks by one item
   6. Repeat same procedure, choose a random item between index 0 and "i",
      and swap with item at position "i".
'''

import random
def list_shuffle(items):
    for i in range(len(items) - 1, 0, -1):
        pick = random.randint(0, i)
        items[pick], items[i] = items[i], items[pick]
    return items

items = ["Anna", "John", "Peter", "Ira", "Bob"]
print(items)
print(list_shuffle(items))

items = list(range(11))
print(items)
print(list_shuffle(items))