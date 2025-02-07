import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(500)
    message = data.decode()

    print(f'message: {message}')

    writer.write(data)
    await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
