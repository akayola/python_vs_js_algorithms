/*
  Calculate Fibonacci number using Dynamic Programming
  Memoization method, saving subproblem solution to object
  O(n) runtime complexity.
  Because its using recursion it may exceed Maximum Call Stack.
*/

class Solution {
    constructor() {
        this.memo = {};
    }
    fib(n, memo) {
        if (n <= 2) return 1;
        if (this.memo[n] !== undefined) {
            return memo[n];
        }
        let result = this.fib(n - 1, this.memo) + this.fib(n - 2, this.memo);
        this.memo[n] = result;
        //console.log(this.memo);
        return result;
    }
}

s = new Solution();

console.log(s.fib(6));
console.log(s.memo);


