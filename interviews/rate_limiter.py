import time
from datetime import timedelta, datetime


class RateLimiter:
    def __init__(self, request_per_minute):
        self.request_per_minute = request_per_minute
        self.request_map = {}

    def is_blocked(self, user_id):
        now = datetime.now()
        count, not_allowed_until = self.request_map.get(user_id, (0, None))
        if not_allowed_until and now < not_allowed_until:
            return True

        if count > self.request_per_minute:
            self.request_map[user_id] = (0, now + timedelta(minutes=1))
            return True

        self.request_map[user_id] = (count + 1, None)
        return False


def main():
    rate_limiter = RateLimiter(5)
    for i in range(70):
        time.sleep(1)
        user_id = 1
        result = rate_limiter.is_blocked(user_id)
        print(result)


if __name__ == '__main__':
    main()
