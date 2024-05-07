function partition(arr, low, high) {
    let pivot = arr[low];
    let start = low + 1;
    let end = high;

    const swap  = (arr, indx1, indx2) => {
        [arr[indx1], arr[indx2]] = [arr[indx1], arr[indx2]];
    };

    while (true) {
        while (start <= end && arr[end] >= pivot) {
            end--;
        }
        while (start <= end && arr[start] <= pivot) {
            start++;
        }
        if (start < end) {
            swap(arr, start, end);
        } else {
            break;
        }
    };
    swap(arr, low, end);
    console.log(arr, pivot, end, low);
    return end;
}

let arr1 = [26, 40, 41, 14, 18, 78, 19, 99];
console.log(partition(arr1, 0, arr1.length - 1));