#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    try:
        obj = load_from_json_file("add_item.json")
    except FileNotFoundError as e:
        obj = None
    if obj is not None:
        for arg in sys.argv[1:]:
            obj.append(arg)
        save_to_json_file(obj, "add_item.json")
    else:
        my_list = list(sys.argv[1:])
        save_to_json_file(my_list, "add_item.json")
    load_from_json_file("add_item.json")
