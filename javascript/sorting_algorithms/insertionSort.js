/* Insertion Sort Algorithm
   Builds up the sort by gradually creating larger left helf,
   which is always sorted.
   It takes element and insert into sorted portion of the array.
   Pseudocode:
   1. Start picking second element in the array.
   2. Compare to element before and swap if necessary, this creates left sorted portion.
   3. Continue to next element compare to previous two sorted elements,
   and if smaller insert into proper position of sorted elements.
   4. Repeat until the array is sorted.
*/

function insertionSort(arr) {
    for (var i = 1; i < arr.length; i++) {
        var currentVal = arr[i];
        for (var j = i - 1; j >= 0 && arr[j] > currentVal; j--) {
            console.log(arr, arr[j], currentVal, i, j);
            arr[j+1] = arr[j];
            console.log(arr, arr[j+1]);
        }
        arr[j+1] = currentVal;
        //console.log(arr, i, j,);
    }
    return arr;
}

console.log(insertionSort([27, 17, 22, 6, 34]));
//console.log(insertionSort([6,5,4,3,2,1]));
