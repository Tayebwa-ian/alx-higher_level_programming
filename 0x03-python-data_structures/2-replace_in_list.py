#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    rn = len(my_list) - 1
    if idx < 0 or idx > rn:
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            my_list[i] = element
    return my_list
