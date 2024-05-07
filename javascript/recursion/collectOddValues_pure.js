/* Collect Odd Values, pure recursion without helper method.
  For array use methods like slice, the spread operator, and concat that make copies of array.
  Strings are immutable, use methods: slice, substr, substring to make copies of strings.
  To make copies of object use Object.assign, or spread operator.
  */


function collectOddValues(arr) {
    // Define empty array on every recursion call
    let newArr = [];

    if (arr.length === 0) {
        return newArr;
    }

    if (arr[0] % 2 !== 0) {
        newArr.push(arr[0]);
    }

    // Concatenate all arrays into newArr
    newArr = newArr.concat(collectOddValues(arr.slice(1)));

    return newArr;
}

console.log(collectOddValues([1,2,3,4,5,6,7,8,9]));
