import functools
import tracemalloc


def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"

        num /= 1024.0

    return f"{num:.1f} Yi{suffix}"


def mem_usage(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        result = func(*args, **kwargs)

        current, peak = tracemalloc.get_traced_memory()
        print(f'Current memory usage: {sizeof_fmt(current)}')
        print(f'Peak memory usage: {sizeof_fmt(peak)}')

        tracemalloc.stop()

        return result

    return wrapper


@mem_usage
def app():
    lt = []
    for i in range(0, 100000):
        lt.append(i)


if __name__ == '__main__':
    app()
