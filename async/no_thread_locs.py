import threading


def process_data(user_data):
    # Do something with user_data
    print(f"Processing data for {user_data['name']} in thread {threading.current_thread().name}")


def worker(user_data):
    process_data(user_data)


def main():
    # Start two threads with different user data
    thread1 = threading.Thread(target=worker, args=({"name": "Alice"},))
    thread2 = threading.Thread(target=worker, args=({"name": "Bob"},))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == '__main__':
    main()
