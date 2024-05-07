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
   O(n) - Best case for already sorted arrays, bacuse current_val < arr[j]  False,
          so algorithm will go to while loop.
   O(n^2) - Worst case for reverse sorted arrays.
*/

function insertionSortWhile(arr) {
    for (let i = 1; i < arr.length; i++) {
        current_val = arr[i];
        j = i - 1;
        while (j >= 0 && current_val < arr[j]) {
            console.log("IN THE WHILE LOOP");
            console.log(arr, current_val, i, j, arr[j], arr[j+1]);
            arr[j + 1] = arr[j];
            j--;
        }
        console.log("OUT of WHILE LOOP");
        console.log(arr, current_val, i, j, arr[j], arr[j+1]);
        arr[j + 1] = current_val;
    }
    return arr;
}

//console.log(insertionSortWhile([5, 20, 40, 60, 10, 30]));
//console.log(insertionSortWhile([10, 20, 30, 40, 50]));
console.log(insertionSortWhile([60,50,40,30,20,10]));
