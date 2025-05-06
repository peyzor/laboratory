from itertools import chain, combinations


def power_set(iterable):
    return chain.from_iterable(combinations(iterable, r) for r in range(len(iterable) + 1))


def my_power_set(iterable):
    if len(iterable) == 0:
        return [[]]

    subsets = []
    first = iterable[0]
    remaining = iterable[1:]

    remaining_subsets = my_power_set(remaining)
    for subset in remaining_subsets:
        subsets.append([first, *subset])
        subsets.append(subset)

    return subsets


def main():
    result = power_set([1, 2, 3])
    print(list(result))

    result = my_power_set([1, 2, 3])
    print(list(result))


if __name__ == '__main__':
    main()
