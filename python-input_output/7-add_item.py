#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
# Importing the necessary functions from external modules
# Note: Make sure to provide proper documentation in the external modules as well.


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
        # Extend the items list with command line arguments (excluding the script name)
    items.extend(sys.argv[1:])
     # Save the updated items list to the JSON file
    save_to_json_file(items, "add_item.json")
