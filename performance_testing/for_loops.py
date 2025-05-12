import timeit
from itertools import repeat


def while_range():
    i = 0
    while True:
        if i == 1_000_000:
            break
        i += 1


def for_range():
    for _ in range(1_000_000):
        pass


def for_repeat():
    for _ in repeat(None, 1_000_000):
        pass


def main():
    while_time = timeit.timeit(while_range, number=100)
    for_time = timeit.timeit(for_range, number=100)
    for_repeat_time = timeit.timeit(for_repeat, number=100)

    print(f'{while_time=:.3f}s')
    print(f'{for_time=:.3f}s')
    print(f'{for_repeat_time=:.3f}s')


if __name__ == '__main__':
    main()
