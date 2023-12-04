#!/usr/bin/python3

if __name__ == "__main__":
    names = ['__init__', 'my_secret_santa', 'print_hidden', 'print_school']
    filtered_names = sorted(name for name in names if not name.startswith('__'))
    for name in filtered_names:
        print(name)
