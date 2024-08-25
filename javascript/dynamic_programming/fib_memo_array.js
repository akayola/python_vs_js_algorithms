/*
  Calculate Fibonacci number using dynamic programming
  Memoization - save subproblem solution and reuse it.
  O(n) runtime complexity.
*/

function fib(n, memo=[]) {
    if (memo[n] !== undefined) return memo[n];
    if (n <= 2) return 1;
    let res = fib(n - 1, memo) + fib(n - 2, memo);
    memo[n] = res;
    console.log(memo);
    return res;
}

console.log(fib(10));
