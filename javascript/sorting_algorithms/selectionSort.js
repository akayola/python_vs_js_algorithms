/* Selection sort algorithms.
   Pseudocode:
   1. Store the first item as the smallest value.
   2. Compare this item to next in the array until find smaller value.
   3. If smaller item is found, designate it as new "minimum" item
      and continue until the end of array.
    4. If the "minimum" is not the value (index) initially began with, swap two items.
    5. Repeat this with the next element until the array is sorted.
    Below algorithm is using nested loop, O(n^2) quadratic runtime complexity (BAD!!!).
    Selection sort algorithms perform little better than Bubble sort algorithms.
*/


function selectionSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        let smallest = i;
        for (let j = i + 1; j < arr.length; j++) {
            //console.log(i, j);
            //console.log(arr, arr[j], arr[smallest], i, j);
            if (arr[j] < arr[smallest]) {
                smallest = j;
            }
        }
        if (i !== smallest) {
            console.log("****************");
            console.log(arr);
            console.log("SWAPPING TO");
            let temp = arr[i];
            arr[i] = arr[smallest];
            arr[smallest] = temp;
            console.log(arr);
            console.log("****************");
        }
    }
    return arr;
}

console.log(selectionSort([23, 16, 56, 18, 67, 32]));
