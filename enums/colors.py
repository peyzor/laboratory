from enum import Enum, Flag, auto


class Color(Enum):
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'


# class ColorFlag(Flag):
#     RED = 1
#     GREEN = 2
#     BLUE = 4
#     YELLOW = 8
#     BLACK = 16

class ColorFlag(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()
    BLACK = auto()
    ALL = RED | GREEN | BLUE | YELLOW | BLACK


def find_color(color):
    match color:
        case Color.RED:
            print('found red')
        case Color.GREEN:
            print('found green')
        case Color.BLUE:
            print('found blue')
        case _:
            print('invalid')


def main():
    print(Color('R'))
    print(Color.RED)
    print(Color.RED.name)
    print(Color.RED.value)

    find_color(Color.BLUE)

    print('#' * 20)
    yellow_and_red = ColorFlag.YELLOW | ColorFlag.RED
    print('combined', yellow_and_red.value)
    for c in yellow_and_red:
        print(c, c.value)

    print('#' * 20)
    print('All')
    for c in ColorFlag.ALL:
        print(c)


if __name__ == '__main__':
    main()
