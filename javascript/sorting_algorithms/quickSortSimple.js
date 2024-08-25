function quickSortSimple(arr) {
    if (arr.length <= 1) return arr;

    let lesser = [];
    let mid = [];
    let greater = [];

    let pivot = Math.floor(arr.length / 2);
    //console.log(pivot);

    for (let i of arr) {
        if (i < arr[pivot]) {
            lesser.push(i);
        }
        if (i === arr[pivot]) {
            mid.push(i);
        }
        if (i > arr[pivot]) {
            greater.push(i);
        }
        quickSortSimple(lesser);
        quickSortSimple(mid);
        quickSortSimple(greater);
    }
    return [].concat(lesser, mid, greater);
}


arr1 = [-2, 14, 4, 29, -5, 10, 1];
console.log(quickSortSimple(arr1));