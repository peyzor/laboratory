import asyncio


async def some_coro(delay):
    await asyncio.sleep(delay)
    print(delay)
    return delay


async def main():
    bg_tasks = set()

    for i in range(5):
        task = asyncio.create_task(some_coro(i))
        bg_tasks.add(task)
        task.add_done_callback(bg_tasks.discard)

    print(bg_tasks)

    for i in range(5):
        await asyncio.sleep(i)

    print(bg_tasks)


if __name__ == '__main__':
    asyncio.run(main())
