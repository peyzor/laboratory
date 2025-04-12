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


def measure_memory_usage(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        result = func(*args, **kwargs)

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics("lineno")

        print(f"Memory usage of {func.__name__}:")
        for stat in top_stats[:5]:
            print(stat)

        return result

    return wrapper


@measure_memory_usage
def app():
    lt = []
    for i in range(0, 100000):
        lt.append(i)

    return lt


if __name__ == '__main__':
    app()
