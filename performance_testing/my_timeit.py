import timeit


def my_sort(x):
    return sorted(x)


def my_reversed_sort(x):
    return sorted(x, reverse=True)


def main():
    setup = """
import random
def my_sort(x):
    return sorted(x)

def my_reversed_sort(x):
    return sorted(x, reverse=True)
    
x = [i for i in range(100, 10_000, 3)]
    """
    stmt = """
random.shuffle(x)
my_sort(x)
    """

    stmt2 = """
random.shuffle(x)
my_reversed_sort(x)
    """

    num = 1000
    x = min(timeit.Timer(stmt=stmt, setup=setup).repeat(repeat=5, number=num))
    y = min(timeit.Timer(stmt=stmt2, setup=setup).repeat(repeat=5, number=num))
    print(x / num)
    print('-' * 20)
    print(y / num)


if __name__ == '__main__':
    main()
