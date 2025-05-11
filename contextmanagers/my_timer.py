import time


class Timer:
    def __init__(self):
        pass

    def __enter__(self):
        self._start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{exc_type=} {exc_val=} {exc_tb=}')
        self._end_time = time.perf_counter()
        elapsed_time = self._end_time - self._start_time
        print(f'elapsed time: {elapsed_time}')
        # return True -> suppress error
        # ich bin nicht dafür
        return True


def main():
    with Timer():
        result = 0
        for x in range(10_000):
            for y in range(x):
                result += 1

        print(result)

    print('#' * 30)

    with Timer():
        result = 0
        for x in range(10_000):
            for y in range(x):
                result += 1

            raise Exception('xd')


if __name__ == '__main__':
    main()
