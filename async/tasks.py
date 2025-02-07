import asyncio
import time


async def say_hello(delay, tg=None):
    await asyncio.sleep(delay)

    t = None
    if tg:
        t = tg.create_task(say_hello(10))

    return delay, t


async def main():
    print(f'started at: {time.strftime('%X')}')

    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_hello(5))
        task2 = tg.create_task(say_hello(3, tg))
        task3 = tg.create_task(say_hello(1))

    x = task1.result()
    print(x)
    y = task2.result()
    print(y)
    z = task3.result()
    print(z)

    print(f'ended at: {time.strftime('%X')}')


if __name__ == '__main__':
    asyncio.run(main())
