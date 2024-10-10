import time


def rate_limit(max_calls, period):
    def decorator(func):
        calls = 0
        last_reset = time.time()

        def wrapper(*args, **kwargs):
            nonlocal calls, last_reset

            elapsed = time.time() - last_reset
            if elapsed > period:
                calls = 0
                last_reset = time.time()

            if calls > max_calls:
                raise Exception('Rate limit exceeded. Please try again later')

            calls += 1

            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limit(max_calls=6, period=10)
def api_call():
    print('API call executed successfully')


def main():
    for _ in range(8):
        try:
            api_call()
        except Exception as e:
            print(f'Error occurred: {e}')


if __name__ == '__main__':
    main()
