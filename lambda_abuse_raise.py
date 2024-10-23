def main():
    l = lambda: (_ for _ in ()).throw(Exception('xd'))
    l()


if __name__ == '__main__':
    main()
