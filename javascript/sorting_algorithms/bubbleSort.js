/* Bubble sorting aglorithms:
   1. Find biggest item and push to end of array.
   2. Perform same with rest of items.
   Using nested loop, O(n^2) runtime complexity (BAD SOLUTION).
   Running from beginning of array, comparing already sorted items.
*/ 

function bubbleSortNestedLoop(arr) {
    for (var i = 0; i < arr.length; i++) {
        for (var j = 0; j < arr.length; j++) {
            console.log(arr, arr[j], arr[j + 1], i, j, j+1);
            if (arr[j] > arr[j+1]) {
                var temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
        console.log("ONE PASS COMPLETE");
    }
    return arr;
}

console.log(bubbleSortNestedLoop([45, 24, 32, 19, 6]));
