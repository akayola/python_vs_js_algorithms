/*
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
*/


function listShuffle(items) {
    for (let i = items.length - 1; i >= 0; i--) {
        let pick = getRandomIntInclusive(0, i);
        swap(items, pick, i);
    }
    return items;
}

function swap(arr, indx1, indx2) {
    [arr[indx1], arr[indx2]] = [arr[indx2], arr[indx1]];
}

function getRandomIntInclusive(min, max) {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled);
}

items = ["Bob", "Jack:", "Peter", "Ira", "Mike", "Anna", "John", "Dona"];
console.log(items);
console.log(listShuffle(items));

let items1 = [];
for (let i = 0; i <= 10; i++) {
    items1.push(i);
}
console.log(items1);
console.log(listShuffle(items1));
