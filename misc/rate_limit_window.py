import collections
import random
import functools
import threading
import time


class RateLimiter:
    def __init__(self, max_calls, period=1.0, callback=None):
        if period <= 0:
            raise ValueError('Rate limiting period should be > 0')

        if max_calls <= 0:
            raise ValueError("Rate limiting number of calls should be > 0")

        self.calls = collections.deque()

        self.period = period
        self.max_calls = max_calls
        self.callback = callback
        self._lock = threading.Lock()

    def __call__(self, f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            with self:
                return f(*args, **kwargs)

        return wrapped

    def __enter__(self):
        with self._lock:
            if len(self.calls) < self.max_calls:
                return

            now = time.time()
            while self.calls and now - self.calls[0] > self.period:
                self.calls.popleft()

            until = now + self.period - self._timespan
            if self.callback:
                t = threading.Thread(target=self.callback, args=(until,))
                t.daemon = True
                t.start()

            wait = until - now
            if wait > 0:
                raise Exception(f'Rate limit exceeded, must wait')

            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with self._lock:
            self.calls.append(time.time())

    @property
    def _timespan(self):
        return self.calls[-1] - self.calls[0]


@RateLimiter(max_calls=3, period=5)
def api_call():
    time.sleep(random.uniform(0.4, 0.7))
    print('API call executed successfully')


def main():
    for i in range(20):
        try:
            print(str(i) + " ", end="")
            api_call()
        except Exception as e:
            time.sleep(random.uniform(0.2, 0.9))  # retry delay
            print(f'Error occurred: {e}')


if __name__ == '__main__':
    main()
