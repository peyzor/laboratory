import asyncio


async def some_coro(delay):
    await asyncio.sleep(delay)
    print(delay)
    return delay


async def main():
    async with asyncio.timeout(5):
        x = await some_coro(6)

    print(x)


if __name__ == '__main__':
    asyncio.run(main())
