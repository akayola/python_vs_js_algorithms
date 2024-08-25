import cProfile

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

cProfile.run('print(fib(5))')

cProfile.run('print(fib(6))')

cProfile.run('print(fib(20))')
