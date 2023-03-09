#!/usr/bin/python3
import importlib
if __name__ == "__main__":
    module = importlib.import_module("hidden_4")
    names = [name for name in dir(module) if not name.startswith("__")]

    for name in sorted(names):
        print(name)
