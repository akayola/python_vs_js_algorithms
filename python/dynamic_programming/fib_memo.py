import cProfile

class Solution:
    def __init__(self):
        self.memo = {}

    def __repr__(self):
        return f'{type(self).__name__}({self.memo!r})'

    def fib(self, n, memo):
        if n <= 2: return 1

        if n in self.memo:
            return self.memo[n]
        else:
            result = self.fib(n - 1, self.memo) + self.fib(n - 2, self.memo)
        self.memo[n] = result
        return result

s = Solution()
cProfile.run('print(s.fib(6, s.memo))')
