import functools


def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if wrapper.instance is None:
            wrapper.instance = cls(*args, **kwargs)

        return wrapper.instance

    wrapper.instance = None
    return wrapper


def besser_singleton(cls):
    instance = None

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)

        return instance

    return wrapper


@besser_singleton
class TheOne:
    pass


if __name__ == '__main__':
    x = TheOne()
    y = TheOne()

    print(id(x))
    print(id(y))

    print(x is y)
