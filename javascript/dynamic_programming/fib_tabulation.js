/*
  Calculate Fibonacci number.
  Using Tabulation approach of dynamic programming (down-up)
  */

function fib(n) {
    if (n <= 2) return 1;
    var fibNums = [0, 1, 1];
    for (let i = 3; i <= n; i++) {
        fibNums[i] = fibNums[i - 1] + fibNums[i - 2];
    }
    //return fibNums[n];
    return fibNums;
}

console.log(fib(6));