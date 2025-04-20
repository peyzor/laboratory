total_conns = 0


async def app(scope, receive, send):
    global total_conns
    total_conns += 1

    curr_conn = total_conns
    print(f'BEGIN CONN: {curr_conn}')
    print(f'SCOPE: {scope}, {receive=} {type(receive)} {send=} {type(send)}')
    print(f'END CONN: {curr_conn}')


def main():
    import uvicorn

    uvicorn.run(
        app,
        port=5000,
        log_level='info',
    )


if __name__ == '__main__':
    main()
