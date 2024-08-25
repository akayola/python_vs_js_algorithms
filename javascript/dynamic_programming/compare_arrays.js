/*
  Compare arrays, using nested loops O(n^2), we should avoid using nested loops!!!

  array.indexOf(element) - method of Array instances returns the first index
  at which a given element can be found in the array,
  if not not present - returns -1;

  splice() - method of Array to remove or replace existing elements, and/or adding new elements.
  splice(start, deleteCount)
  start - index at which start changing the array
  deleteCount - number of elements in the array to remove from start
*/

function same(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return false;
    }
    for (let i = 0; i < arr1.length; i++) {
        let correctIndex = arr2.indexOf(arr1[i] ** 2);
        if (correctIndex === -1) {
            return false;
        }
        console.log(arr2);
        arr2.splice(correctIndex, 1);
    }
    return true;
}

console.log(same([3, 4, 5, 6], [16, 36, 9, 25]));
console.log(same([3, 4, 5, 6], [1, 16, 25, 36]));