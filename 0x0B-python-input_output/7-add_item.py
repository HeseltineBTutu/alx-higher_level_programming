#!/usr/bin/python3
"""
A module adds all arguments to a Python list
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    arguments = sys.argv[1:]

    try:
        existing_data = load_from_json_file('add_item.json')
    except FileNotFoundError:
        # If the file does't exist, start with an empty list
        existing_data = []
        # Add new arguments to the existing list
    existing_data.extend(arguments)
    # Save the updated list to add_item.json
    save_to_json_file(existing_data, 'add_item.json')
