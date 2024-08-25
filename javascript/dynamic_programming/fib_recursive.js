/*
  Calculate Fibonacci number using recursion.
O(2^n) exponential runtime complexity
*/

function fib(n) {
    if ( n <= 2) return 1;
    return fib(n - 1) + fib(n - 2);
}

console.log(fib(6));