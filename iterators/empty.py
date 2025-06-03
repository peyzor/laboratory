def my_not_so_empty_generator():
    yield


def my_empty_generator():
    yield from ()


def my_weird_empty_generator():
    # yes, this works
    return
    yield  # noqa


def main():
    print(list(my_not_so_empty_generator()))
    print(list(my_empty_generator()))
    print(list(my_weird_empty_generator()))


if __name__ == '__main__':
    main()
