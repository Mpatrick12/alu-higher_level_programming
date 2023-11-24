#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""

import sys

# Importing the necessary functions from external modules
# Note: Make sure to provide proper documentation in the external modules as well.

# Importing the save_to_json_file function from the 5-save_to_json_file module
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# Importing the load_from_json_file function from the 6-load_from_json_file module
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    # Attempt to load existing items from the JSON file
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file is not found, initialize an empty list
        items = []

    # Extend the items list with command line arguments (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated items list to the JSON file
    save_to_json_file(items, "add_item.json")
