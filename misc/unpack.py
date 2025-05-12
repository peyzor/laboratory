def main():
    # it's impossible for unpacking to be the same type as source
    # the implementation is impossible, so they settle for returning a
    # list all the time even when the source is a text, tuple or ...
    text = 'hello'
    a, *b = text
    print(f'{a=} {type(a)=}')
    print(f'{b=} {type(b)=}')

    x = text[0]
    y = text[1:]
    print(f'{x=} {type(x)=}')
    print(f'{y=} {type(y)=}')

    f, *d = (1, 2, 3, 4, 5)
    print(f'{f=} {type(f)=}')
    print(f'{d=} {type(d)=}')


if __name__ == '__main__':
    main()
