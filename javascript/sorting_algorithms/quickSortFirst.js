function partition(arr, start, end) {
    let pivot = arr[start];
    let swapIndex = start;

    const swap = (arr, indx1, indx2) => {
        [arr[indx1],arr[indx2]] = [arr[indx2],arr[indx1]];
    };

    for (let i = start + 1; i < arr.length; i++) {
        if (pivot > arr[i]) {
            swapIndex++;
            swap(arr, swapIndex, i);
            //swapIndex++;
        }
    }
    swap(arr, start, swapIndex);
    return swapIndex;
}

function quickSort(arr, start, end) {
    if (start < end) {
        let pivotIndex = partition(arr, start, end);
        quickSort(arr, start, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, end);
    }
    return arr;
}

//let arr1 = [26, 40, 41, 14, -18, 78, 19, 99, -10];
let arr1 = [0,1,2,3,4,5,6,7,8,9];

//let arr1 = [10,9,8,7,6,5,4,3,2,1,0];
//let arr1 = [9,0,-1];

console.log(quickSort(arr1, 0, arr1.length - 1));

