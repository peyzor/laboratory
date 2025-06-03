from itertools import count, cycle, repeat, chain


def my_cycle(iterable):
    i = 0
    while True:
        yield iterable[i % len(iterable)]
        i += 1


def main():
    counter = count(0.0, 0.5)
    print(next(counter))
    print(next(counter))
    print(next(counter))
    print(next(counter))

    people = ['bob', 'james', 'joe', 'sandra']
    people_cycle = cycle(people)
    for _ in range(12):
        print(next(people_cycle), end=' ')
    print()

    print('#' * 25)
    people_cycle = my_cycle(people)
    for _ in range(12):
        print(next(people_cycle), end=' ')
    print()

    print('#' * 25)
    infinite = repeat('Bob')
    print(next(infinite))
    print(next(infinite))
    print(next(infinite))
    print(next(infinite))

    my_chain = chain([1, 2, 3], [4, 5])
    print(list(my_chain))

    my_nested_chain = chain.from_iterable([[1, 2, 3], [4, 5]])
    print(list(my_nested_chain))


if __name__ == '__main__':
    main()
