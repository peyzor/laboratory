import functools
import threading
import time
from collections import OrderedDict


def conditional_cache(_func=None, *, expiry=5, condition=None, max_size=5):
    # testing new ssh keys
    if not condition:
        condition = lambda *args, **kwargs: True

    cache_data = OrderedDict()
    cache_lock = threading.Lock()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = (*args, *tuple(kwargs.items()))
            current_timestamp = time.time()

            if not condition(*args, **kwargs):
                return None

            with cache_lock:
                if cache_key in cache_data:
                    cached_value, cached_time = cache_data[cache_key]
                    if current_timestamp - cached_time < expiry:
                        cache_data.move_to_end(cache_key)
                        return cached_value
                    else:
                        del cache_data[cache_key]

                result = func(*args, **kwargs)

                cache_data[cache_key] = (result, current_timestamp)

                if len(cache_data) > max_size:
                    cache_data.popitem(last=False)

            return result

        return wrapper

    if _func is not None:
        return decorator(_func)

    return decorator
