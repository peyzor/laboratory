import functools


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.func(*args, **kwargs)


@CountCalls
def fib(n):
    if n < 2:
        return 1

    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    fib(10)
    print(fib.call_count)
