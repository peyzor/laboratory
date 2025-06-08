import os
from pathlib import Path


def main():
    print(os.path.dirname(os.path.abspath(__file__)))
    print(Path(__file__).resolve().parent)
    print(Path.cwd())
    print('#' * 20)

    print(Path().resolve().parent)
    print('#' * 20)
    for p in Path().resolve().parent.iterdir():
        print(p)

    print('#' * 20)
    my_dir = Path('my_dir')
    my_file = Path('file.txt')
    print(my_file.name)
    print(my_file.stem)
    print(my_file.suffix)

    print(os.path.join(my_dir.resolve(), 'new_file.txt'))
    new_file = my_dir / 'new_file.txt'
    print(new_file.resolve())
    print(new_file.exists())
    new_file2 = my_dir.joinpath('new_file.txt')
    print(new_file2.resolve())

    print(my_dir.absolute())
    print(my_dir.parent.absolute())

    # resolves symlinks and gives the absolute path
    print(my_dir.resolve())
    print(my_dir.parent.resolve())

    print(Path('..').resolve())
    # does not understand
    print(Path('..').absolute())

    print(Path('~/dotfiles').expanduser())
    print(Path.home() / 'dotfiles')

    print('#' * 20)
    dotfiles = Path.home() / 'dotfiles'
    # use rglob for recursive glob
    for p in dotfiles.glob('*vim*', case_sensitive=False):
        print(p)

    print('#' * 20)
    ideavimrc = Path.home() / 'dotfiles' / 'ideavimrc'
    with ideavimrc.open() as f:
        print(f.read())

    # p = Path('tempdir')
    # p.mkdir()
    # p.rmdir()

    # p = Path('tempdir/subdir')
    # p.mkdir(parents=True)

    # p = Path('tempfile.txt')
    # p.touch()

    # p = Path('tempfile.txt')
    # p.touch()
    # p.rename('temp_file.txt')

    # p = Path('tempfile.txt')
    # p.touch()
    # p.replace('temp_file.txt')

    # p = Path('tempfile.txt')
    # p.touch()
    # p.unlink()





if __name__ == '__main__':
    main()
