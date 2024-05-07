// Binary search only works on sorted arrays.
// O(logn) runtime complexity.

function binarySearch(arr, val) {
    let start = 0;
    let end = arr.length -1;
    while (start <= end) {
        let mid = Math.floor((start + end) / 2);
        //console.log(mid);
        if (arr[mid] > val) {
            end = mid - 1;
        } else if (arr[mid] < val) {
            start = mid + 1;
        } else {
            return mid;
        }
    }
    return null;
}

let states = [
              "Alabama",
              "Alaska",
              "Arizona",
              "Arkansas",
              "California",
              "Colorado",
              "Connecticut",
              "Delaware",
              "Florida",
              "Georgia",
              "Hawaii",
              "Idaho",
              "Illinois",
              "Indiana",
              "Iowa",
              "Kansas",
              "Kentucky",
              "Louisiana",
              "Maine",
              "Maryland",
              "Massachusetts",
              "Michigan",
              "Minnesota",
              "Mississippi",
              "Missouri",
              "Montana",
              "Nebraska",
              "Nevada",
              "New Hampshire",
              "New Jersey",
              "New Mexico",
              "New York",
              "North Carolina",
              "North Dakota",
              "Ohio",
              "Oklahoma",
              "Oregon",
              "Pennsylvania",
              "Rhode Island",
              "South Carolina",
              "South Dakota",
              "Tennessee",
              "Texas",
              "Utah",
              "Vermont",
              "Virginia",
              "Washington",
              "West Virginia",
              "Wisconsin",
              "Wyoming"
            ];

console.log(binarySearch([1,3,4,5,8,10,12,15,16,21,34,41], 21));
console.log(binarySearch([1,3,4,5,8,10,12,15,16,21,34,41], 22));
console.log(binarySearch(states, "North Dakota"));
