#!/usr/bin/python3
"""
A module adds all arguments to a Python list
"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


# Getting the command-line arguments excluding the script name
arguments = sys.argv[1:]

try:
    # Load existing data from file if available
    existing_data = load_from_json_file('add_item.json')
except FileNotFoundError:
    # If the file does't exist, start with an empty list
    existing_data = []

# Add new arguments to the existing list
existing_data.extend(arguments)

# Save the updated list to add_item.json
save_to_json_file(existing_data, 'add_item.json')
