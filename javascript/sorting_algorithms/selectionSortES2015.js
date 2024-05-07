/* Selection sort with ES2015 swap syntax
   Pseudocode:
   1. Store the first item as the smallest value.
   2. Compare this item to next in the array until find smaller value.
   3. If smaller item is found, designate it as new "minimum" item
      and continue until the end of array.
   4. If the "minimum" is not the value (index) initially began with, swap two items.
   5. Repeat this with the next element until the array is sorted.
   ßBelow algorithm is using nested loop, O(n^2) quadratic runtime complexity (BAD!!!).
*/

function selectionSortES2015(arr) {
    const swap = (arr, indx1, indx2) => {
        [arr[indx1], arr[indx2]] = [arr[indx2], arr[indx1]];
    };
    for (let i = 0; i < arr.length; i++) {
        smallest = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[smallest]) {
                smallest = j;
            }
        }
        console.log("***********");
        console.log(arr);
        console.log("SWAPPING TO");
        if (i !== smallest) swap(arr, i, smallest);
        console.log(arr);
        console.log("**********");
    }
    return arr;
}

console.log(selectionSortES2015([23, 15, 56, 34, 7, 19]));