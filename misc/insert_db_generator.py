from unittest import mock


class CommitException(Exception):
    pass


class AbortException(Exception):
    pass


class AddToDBCtx:
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        next(self.gen)
        return self.gen

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.gen.close()
        return


def add_to_database():
    db = mock.MagicMock()
    cursor = db.cursor()
    cursor.execute.side_effect = lambda x: print(x)

    try:
        while True:
            try:
                row = yield
                cursor.execute('INSERT INTO mytable VALUES({}, {}, {})'.format(*row))  # noqa
            except CommitException as e:
                print(e)
                cursor.execute('COMMIT')
            except AbortException as e:
                print(e)
                cursor.execute('ABORT')
    finally:
        cursor.execute('ABORT FINALLY')
        db.close()


def main():
    with AddToDBCtx(add_to_database()) as coroutine:
        coroutine.send(('v1', 'v2', 'v3'))
        coroutine.send(('v4', 'v5', 'v6'))
        coroutine.throw(CommitException('commit now'))
        coroutine.send(('v7', 'v8', 'v9'))
        coroutine.throw(AbortException('abort now'))


if __name__ == '__main__':
    main()
