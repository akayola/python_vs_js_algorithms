import cProfile

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

class Solution:
    def __init__(self):
        # initialize memo
        self.memo = {}


    def fib(self, n: int) -> int:
        # base case
        if n < 2:
            return n

        # check if fib(n) is already in memo - f(n) was calculated before
        if n in self.memo:
            return self.memo[n]
        else:
            f = self.fib(n - 1) + self.fib(n - 2)

        # store the value of fib(n) when calculated 
        self.memo[n] = f 
   
        return f

cProfile.run('print(fib(6))')

s = Solution()
cProfile.run('print(s.fib(6))')
