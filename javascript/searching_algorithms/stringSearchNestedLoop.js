/* Searching sub-string using nested loop.
O(n**2) - quadratick runtime complexity (BAD SOLUTION!!!).
Pseudocode:
1. Loop over string
2. Loop over pattern string
3. If the charactes don't match, break out inner loop.
4. If the characters match, keep going.
5. If searching inner loop complete and foud match, increment cout.
6. Return count. 
   */

function stringSearchNestedLoop(long, pattern) {
    let count = 0;
    for (i = 0; i < long.length; i++) {
        for (j = 0; j < pattern.length; j++) {
            console.log(long[i], pattern[j], i, j);
            if (pattern[j] !== long[i+j]) {
                console.log("BREAK!");
                break;
            }
            // Increment count if j is equal to lenght of pattern.
            if (j === pattern.length - 1) {
                count++;
            }
        }
    }
    return count;
}

console.log(stringSearchNestedLoop("create lollipop charts with pandas, matplotlib and lol", "lol"));