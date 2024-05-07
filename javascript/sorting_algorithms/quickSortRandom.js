const swap = (arr, indx1, indx2) => {
    [arr[indx1],arr[indx2]] = [arr[indx2],arr[indx1]];
}

function randomPivotIndx(arr, start, end) {
    let randomPivot = Math.floor(Math.random() * (end - start + 1) + start);
    swap(arr, start, randomPivot);
    return partition(arr, start, end);
}

function partition(arr, start, end) {
    let pivot = arr[start];
    let swapIndex = start + 1;
    for (let i = start + 1; i <= arr.length + 1; i++) {
        if (pivot >= arr[i]) {
            swap(arr, i, swapIndex);
            swapIndex++;
        }
    }
    swap(arr, start, swapIndex - 1);
    return swapIndex - 1;
}

function quickSort(arr, start, end) {
    if (start < end) {
        let pivotIndex = randomPivotIndx(arr, start, end);
        quickSort(arr, start, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, end);
    }
    return arr;
}

let arr1 = [12, -2, 16, 22, 65, -4, 19, 34];
console.log(quickSort(arr1, 0, arr1.length - 1));