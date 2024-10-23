class ResetException(Exception):
    pass


def my_gen():
    try:
        yield 10
        print('state 1')
        yield 20
        print('state 2')
        yield 30
        print('state 3')
    except ResetException as e:
        print(e)
        yield my_gen()


def main():
    g = my_gen()
    print(next(g))
    print(next(g))
    g = g.throw(ResetException('must reset'))
    print(next(g))


if __name__ == '__main__':
    main()
