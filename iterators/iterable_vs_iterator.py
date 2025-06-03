class MyRangeIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration('stop my man')

        val = self.current
        self.current += 1
        return val


class MyRangeIterator1:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    # def __iter__(self):
    #     return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration('stop my man')

        val = self.current
        self.current += 1
        return val


class MyRangeIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangeIterator1(self.start, self.end)


class MyAmazingRangeIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for i in range(self.start, self.end):
            yield i


def main():
    for i in MyRangeIterable(3, 6):
        print(i)

    print('-' * 20)
    for i in MyRangeIterator(3, 6):
        print(i)

    print('-' * 20)
    for i in MyAmazingRangeIterable(3, 6):
        print(i)


if __name__ == '__main__':
    main()

# >>> for item in SequenceIterator([1, 2, 3, 4])

# UNDER THE HOOD
# >>> sequence = SequenceIterator([1, 2, 3, 4])
#
# >>> # Get an iterator over the data
# >>> iterator = sequence.__iter__()
# >>> while True:
# ...     try:
# ...         # Retrieve the next item
# ...         item = iterator.__next__()
# ...     except StopIteration:
# ...         break
# ...     else:
# ...         # The loop's code block goes here...
# ...         print(item)