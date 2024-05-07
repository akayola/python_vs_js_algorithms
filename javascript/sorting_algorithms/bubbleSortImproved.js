/* Sort array using nested loop.
   O(n**2) runtime complexity (BAD SOLUTION).
   Running from the end of array, at least doesn't compare already sorted items.
*/

function bubbleSortNestedLoopImproved(arr) {
    for (var i = arr.length; i > 0; i--) {
        for (var j = 0; j < i - 1; j++) {
            console.log(arr, arr[j], arr[j+1], i, j, j+1);
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

console.log(bubbleSortNestedLoopImproved([45, 24, 32, 19, 6]));
