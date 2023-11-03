#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    rn = len(my_list) - 1
    if idx < 0 or idx > rn:
        return my_list
    else:
        my_list[idx] = element
        return my_list
