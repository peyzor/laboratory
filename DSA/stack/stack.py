class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def pop(self):
        if len(self.items) == 0:
            return None

        return self.items.pop()

    def peek(self):
        return self.items[-1]


def is_balanced(string):
    stack = []
    for ch in string:
        if ch != ')':
            stack.append(ch)
            continue

        top = stack.pop() if len(stack) > 0 else None
        if top != '(':
            return False

    if len(stack) != 0:
        return False

    return True


def main():
    x = '()())'
    y = '((()))'
    z = '(()(()))'
    r = '('
    for string in (x, y, z, r):
        print(is_balanced(string))


if __name__ == '__main__':
    main()
