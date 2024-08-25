/*
  Quick sort using first element as pivot
*/

//function pivot(arr, start=0, end=arr.length + 1) {
function pivot(arr, start, end) {
    let pivot = arr[start];
    let swapIndex = start;

    const swap = (arr, indx1, indx2) => {
        [arr[indx1],arr[indx2]] = [arr[indx2],arr[indx1]];
    }
    // Compare pivot to each element
    for (let i = start + 1; i < arr.length; i++) {
        if (pivot > arr[i]) {
            swapIndex++;
            swap(arr, swapIndex, i);
            //console.log(arr);
        }
    }
    //Swap pivot with element with swapIndex
    swap(arr, start, swapIndex);
    //console.log(arr, pivot);
    return swapIndex;
}

//console.log(pivot([4, 8, 2, 1, 5, 7, 6, 3]));

//function quickSort(arr, left=0, right = arr.length - 1) {
function quickSort(arr, left, right) {
    if (left < right) {
        let pivotIndex = pivot(arr, left, right);
        //left
        quickSort(arr, left, pivotIndex - 1);
        //right
        quickSort(arr, pivotIndex + 1, right);
    }
    return arr;
}

//let arr1 = [4, 8, 2, 1, 5, 7, 6, 3];
let arr1 = [10,9,8,7,6,5,4,3,2,1,0];
console.log(quickSort(arr1, 0, arr1.length - 1));
