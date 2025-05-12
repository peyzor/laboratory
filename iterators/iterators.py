from itertools import count, cycle, repeat


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


if __name__ == '__main__':
    main()
