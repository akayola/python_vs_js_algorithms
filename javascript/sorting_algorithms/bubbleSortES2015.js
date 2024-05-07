/* Sort array using nested loop.
   O(n**2) runtime complexity (BAD SOLUTION).
   Running from the end of array, at least doesn't compare already sorted items.
*/

function bubbleSortNestedLoopImproved(arr) {
    const swap = (arr, indx1, indx2) => {
        [arr[indx1], arr[indx2]] = [arr[indx2], arr[indx1]];
    };

    for (let i = arr.length; i > 0; i--) {
        for (let j = 0; j < i - 1; j++) {
            console.log(arr, arr[j], arr[j+1], i, j, j+1);
            if (arr[j] > arr[j+1]) {
                swap(arr, j, j + 1);
            }
        }
        console.log("ONE PASS COMPLETE");
    }
    return arr;
}

console.log(bubbleSortNestedLoopImproved([45, 24, 32, 19, -6]));