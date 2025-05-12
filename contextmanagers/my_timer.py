import time
import datetime
from contextlib import contextmanager


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
        # return True suppresses the error
        # ich bin nicht dafür
        return True


@contextmanager
def my_timer():
    print(f'started at: {datetime.datetime.now():%H:%M:%S}')
    print(f'started at: {datetime.datetime.now().strftime('%H:%M:%S')}')
    start_time = time.perf_counter()
    try:
        yield
    finally:
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f'ended at: {datetime.datetime.now().strftime('%H:%M:%S')}')
        print(f'elapsed time: {elapsed_time:.4f}s')


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

    print('#' * 30)

    with my_timer():
        result = 0
        for x in range(10_000):
            for y in range(x):
                result += 1

        print(result)


if __name__ == '__main__':
    main()
