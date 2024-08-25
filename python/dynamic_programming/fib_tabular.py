import cProfile

class Solution:
    def __init__(self):
        self.fibNums = []

    def fib(self, n):

        if n <= 2: return 1

        self.fibNums = [0, 1, 1]

        for i in range(3, n + 1):
            self.fibNums.append(self.fibNums[i - 1] + self.fibNums[i - 2])

        return self.fibNums

s = Solution()

cProfile.run('print(s.fib(6))')
