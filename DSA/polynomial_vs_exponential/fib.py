# naive recursive
def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)

def fib_iterative(n):
    if n == 0 or n == 1:
        return n

    grandparent = 0
    parent = 1
    current = 0
    for i in range(n - 1):
        current = grandparent + parent
        grandparent = parent
        parent = current

    return current


def main():
    for i in range(10):
        print(fib(i), sep=' ')

    print()

    for i in range(10):
        print(fib_iterative(i), sep=' ')

    print()


if __name__ == '__main__':
    main()
