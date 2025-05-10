import random


class HashMap:
    def __init__(self, size):
        self.items = [None for i in range(size)]

    def __repr__(self):
        result = ''
        for item in self.items:
            if not item:
                continue

            key, val = item
            result += f'{key}: {val}\n'

        return result

    def insert(self, key, value):
        index = self.key_to_index(key)
        self.items[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        item = self.items[index]
        if not item:
            raise KeyError(f'not found')

        return item[1]

    def key_to_index(self, key):
        sum_ = 0
        for c in key:
            sum_ += ord(c)

        return sum_ % len(self.items)


def main():
    hashmap = HashMap(64)
    for i in ['asdf', 'xd', 'dx', 'yz', 'yz', 'dxy']:
        hashmap.insert(i, random.randrange(30, 39))

    print(hashmap)
    print(hashmap.get('yz'))
    print(hashmap.get('xd'))

    try:
        hashmap.get('vvv')
    except KeyError as e:
        print(e)


if __name__ == '__main__':
    main()
